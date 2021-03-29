<template>
  <v-container fluid id="main_day">
    <v-main>
      <v-container fluid >
        <h4 class="mb-5" id="title_day" justify="center">Количество ДТП по анализируемому параметру посуточно</h4>  
        <v-row id="first_day">
          <v-col lg="4" cols="12" sm="6" class="pa-1 ma-0"
            ><v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              max-width="490px"
              min-width="390px"
              class="ma-0 pa-0"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :value="monthes"
                  label="Дата"
                  append-icon="mdi-calendar"
                  color="green lighten-1"
                  height="45px"
                  dense
                  outlined
                  item-color="green lighten-1"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                @change="generateUrl"
                v-model="monthes"
                type="month"
                color="green lighten-1 lighten-1"
                min="2015-01"
                max="2020-11"
                scrollable
                locale="ru"
                full-width
                no-title
              >
              </v-date-picker> </v-menu
          ></v-col>

          <v-col lg="4" sm="6" cols="12" class="pa-1 ma-0" 
            ><v-select
              @change="generateUrl"
              v-model="selectedSubject"
              label="Субъект(ы)"
              color="green lighten-1"
              height="45px"
              item-color="green lighten-1"
              outlined
              :items="sortSubjects"
              menu-props="auto"
              item-text="title"
              item-value="id"
              multiple
              dense
              class="ma-0 pa-0"
            >
              <template v-slot:selection="{ item, index }">
                <v-chip v-if="index === 0" small>
                  <span>{{ item.title }}</span>
                </v-chip>
                <span v-if="index === 1" class="grey--text caption">
                  (+{{ selectedSubject.length - 1 }} других)
                </span>
              </template>
              <template v-slot:prepend-item>
                <v-list-item @change="generateUrl" ripple @click="toggle">
                  <v-list-item-action>
                    <v-icon
                      :color="
                        selectedSubject.length > 0 ? 'green lighten-1' : ''
                      "
                      >{{ icon }}</v-icon
                    >
                  </v-list-item-action>
                  <v-list-item-title>Выбрать все</v-list-item-title>
                </v-list-item>
                <v-divider class="mt-2" />
              </template> </v-select
          ></v-col>
          <v-col lg="4" sm="12" cols="12" class="pa-1 ma-0"
            ><v-select
              id="par_day"
              color="green lighten-1"
              outlined
              item-color="green lighten-1"
              dense
              height="45px"
              @change="setPar"
              v-model="selectedPar"
              label="Анализируемый параметр"
              :items="parameters"
              item-text="text"
              return-object
              class="ma-0 pa-0"
          /></v-col>
        </v-row>
        <v-progress-circular
          v-show="progressBar"
          slot="progress"
          color="green lighten-1"
          indeterminate
        ></v-progress-circular>
      </v-container>
      <h4 justify="center" class="font-weight-light">{{selectedPar.text}} в одном ДТП</h4>
      <column-chart
      
        v-if="!progressBar"
        :download="selectedPar.text"
        ytitle="Количество ДТП"
        xtitle="Дата"
        :messages="{ empty: 'Выберите параметр' }"
        :data="parCount"
        :stacked="true"
      >
      </column-chart>
    </v-main>
  </v-container>
</template>

<script>
import axios from "axios";
import Chartkick from "vue-chartkick";
// import Chart from "chart.js";

// import Header from "@/components/Header";

// import { yandexMap, ymapMarker , loadYmap} from "vue-yandex-maps";
export default {
  name: "GraphDay",
  components: {},
  computed: {
    likesAllSubjects() {
      return this.selectedSubject.length === this.subjects.length;
    },
    likesSomeSubjects() {
      return this.selectedSubject.length > 0 && !this.likesAllSubjects;
    },
    icon() {
      if (this.likesAllSubjects) return "mdi-close-box";
      if (this.likesSomeSubjects) return "mdi-minus-box";
      return "mdi-checkbox-blank-outline";
    },
    sortSubjects: function () {
      function subjectsTitle(a, b) {
        if (a.title < b.title) return -1;
        if (a.title > b.title) return 1;
        return 0;
      }
      return [...this.subjects].sort(subjectsTitle); // shallow clone + sort
    },
  },

  methods: {
    changeSeparate() {},
    toggle() {
      this.$nextTick(() => {
        if (this.likesAllSubjects) {
          this.selectedSubject = [];
        } else {
          this.selectedSubject = this.subjects.slice();
        }
      });
    },
    generateUrl() {
      // this.selectedPar = {};
      this.progressBar = true;

      this.url = "http://127.0.0.1:8000/api/incident/incidentsG/?";
      var startYM,
        endYM,
        startArr,
        endArr,
        startDate,
        endDate = "";
      // console.log(endYM);

      startYM = this.monthes;
      startArr = startYM.split("-");
      startDate = new Date(startArr[0], startArr[1] - 1, 1).toLocaleDateString(
        "en-CA"
      );

      endDate = new Date(startArr[0], startArr[1], 0).toLocaleDateString(
        "en-CA"
      );

      console.log("st" + startDate);
      console.log("end" + endDate);
      // if(this.selectedTime.start===undefined){
      //  this.selectedTime.start  = '';
      //   this.selectedTime.end = '';
      // }
      this.url +=
        "start_date=" +
        startDate +
        "&end_date=" +
        endDate +
        "&id_address__id_road__id_locality__id_district__id_subject=" +
        this.selectedSubject.join();
      console.log("Url");
      console.log(this.url);
      this.readDataFromAPI(this.url);
    },
    // console.log(result)

    readDataFromAPI(url) {
      axios
        .get(url + "&limit=100000&offset=0")

        .then((response) => {
          //Then injecting the result to datatable parameters.
          this.items = response.data.results;

          console.log("items");
          console.log(this.items);
          console.log(url + "&limit=100000&offset=0");

          this.totalItems = response.data.count;
          this.progressBar = false;
          this.setPar();

          // this.headers = this.getHeaders(this.items[0]);
        });
    },
    getSubjects() {
      axios
        .get(this.url + "/?limit=" + 100 + "&offset=" + 0)
        .then((response) => {
          this.subjects = response.data.results;
          console.log("SUBJ");
          console.log(this.subjects);
        });
    },
    setPar() {
      console.log(this.selectedPar.value);
      let par = this.selectedPar.value;
      console.log("par " + par);
    //   {name: 'Workout', data: {'2017-01-01 00:00:00 -0800': 3, '2017-01-02 00:00:00 -0800': 4}},
        this.parCount = [];
        for (let i = 0; i < this.items.length; i++) {
          var key = this.items[i][par].toString();
          var date = this.items[i]["date"];
          var index = this.parCount.map((x) => x.name).indexOf(key);

          if (index != -1) {
              let obj = this.parCount[index]['data'][date]
              if(obj != undefined){
                  this.parCount[index]['data'][date]++

              }
              else{
                  this.parCount[index]['data'][date] = 1
              }
              //   let keyInArr = this.parCount[index]["items"].find(o => o.key == key)

            //   if (this.parCount[index]["items"].find(o => o.key == key).key != undefined) {
            //     this.parCount[index]["items"].find((o) => o.key == key).count++;
            //   } else {
            //     this.parCount[index]["items"].push({ key: key, count: 1 });
            //   }
          } else {
            this.parCount.push({ name: key, data: { [date]: 1 } });
          }
          // var b = Object.keys()
          //   if (this.parCount[a] != undefined) ++this.parCount[a];
          //   else this.parCount[a] = 1;
          // }
        }
        this.parCount.sort((a, b) => a.name.localeCompare(b.name));

      console.log(this.parCount);
    },
  },
  data() {
    return {
      url: "http://127.0.0.1:8000/api/incident/subjects",
      urlD: "http://127.0.0.1:8000/api/incident/districts/?id_subject__id=",
      monthes: "2015-01",
      subjects: [],
      selectedSubject: [15],
      types: [],
      selectedType: [],
      items: [],
      item: [],
      options: {},
      totalItems: 0,
      progressBar: false,
      parCount: {},

      parameters: [
        { text: "Количество погибших", value: "deaths" },
        { text: "Количество раненых", value: "wounds" },
        { text: "Количество видов происшествий", value: "id_type__value" },
        { text: "Количество ТС", value: "transport__count" },
        { text: "Количество участников ", value: "participant__count" },
        { text: "Погодные условия", value: "weathers" },
        { text: "Освещение", value: "id_lighting__value" },
        {
          text: "Состояние дорожного покрытия",
          value: "id_roadwayStatus__value",
        },
      ],
      selectedPar: { text: "Количество погибших", value: "deaths" },

      headers: [
        {
          text: "#",
          value: "id",
        },
        {
          text: "Район",
          value: "id_address__id_road__id_locality__id_district__title",
        },
        {
          text: "Населенный пункт",
          value: "id_address__id_road__id_locality__title",
        },
        { text: "Дата", value: "date" },
        { text: "Время", value: "time" },
        { text: "Тип происшествия", value: "id_type__value" },
        { text: "Участники", value: "participant__count" },
        { text: "ТС", value: "transport__count" },

        { text: "Раненые", value: "wounds" },
        { text: "Погибшие", value: "deaths" },
        { text: "Широта", value: "id_address__latitude" },
        { text: "Долгота", value: "id_address__longtitude" },
      ],
      menu: false,
      modal: false,
      dialog: false,
      coords: [],
    };
  },
  watch: {
    parCount() {
      this.progressBar = false;
    },
    options: {
      handler() {
        this.readDataFromAPI(this.url);
      },
    },
    deep: true,
    // selectedSubject: {
    //   handler() {
    //     this.getDistricts(this.selectedSubject);
    //   },
    //   immediate: true,

    //   deep: true,
    // },
  },
  afterCreate() {},
  created() {
    this.getSubjects();
  },
  mounted() {
    this.generateUrl();

    // const settings = { lang: 'ru_RU' };
    // loadYmap(settings);
    // console.log(loadYmap); // здесь доступен весь функционал ymaps
    // this.coords =[75.45, 54.31]
  },
  updated() {},
};
</script>
<style scoped>
* {
  font-family: "Ubuntu", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
#app {
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}

#button {
  width: 100%;
}
#main_day{
    padding: 1px;
    border: 0.5px lightgray;
    border-style: solid;
    border-radius: 5px;
}
area-chart {
  transition: opacity 2s ease-in;
}
.data_container {
  padding: 0px;
}
.container--fluid{
  max-width: 99%;
   margin-top: 5px;
  margin-bottom: 0;
  padding-bottom: 0;
}
.v-text-field.v-text-field--enclosed >>> .v-text-field__details{
    margin-bottom: 0 !important;
}
.v-input >>> .v-input__control >>> .v-text-field__details{
    display: none !important;
}
</style>