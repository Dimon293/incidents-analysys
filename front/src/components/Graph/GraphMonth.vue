<template>
  <v-container fluid id="main_month">
      <v-main>
        <v-container fluid>
            <h4 class="mb-5" id="title_month" justify="center">Количество ДТП по анализируемому параметру</h4>  

          <v-row id="first">
            <v-col lg="3" cols="12" sm="6" class="pa-1 ma-0"
              ><v-menu
                ref="menu"
                v-model="menu"
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                max-width="490px"
                min-width="390px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    :value="sortDate"
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
                  range
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

            <v-col lg="3" sm="6" cols="12" class="pa-1 ma-0"
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
                        :color="selectedSubject.length > 0 ? 'green lighten-1' : ''"
                        >{{ icon }}</v-icon
                      >
                    </v-list-item-action>
                    <v-list-item-title>Выбрать все</v-list-item-title>
                  </v-list-item>
                  <v-divider class="mt-2" />
                </template> </v-select
            ></v-col>

            <v-col lg="3" sm="6" cols="12" class="pa-1 ma-0"
              ><v-select
                id="time"
                color="green lighten-1"
                outlined
                item-color="green lighten-1"
                dense
                height="45px"
                @change="setPar"
                v-model="selectedTime"
                label="Временной интервал"
                :items="time"
                item-text="text"
                return-object
              />
            </v-col>
            <v-col lg="3" sm="6" cols="12" class="pa-1 ma-0"
              ><v-select
                id="par"
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
            /></v-col>
          </v-row>
          <v-progress-circular
          
            v-show="progressBar"
            slot="progress"
            color="green lighten-1"
            indeterminate
          ></v-progress-circular>
        </v-container>
          <h4 v-if="selectedTime.value" justify="center" class="font-weight-light">Время суток</h4>  
        <column-chart 
        v-if="!progressBar"
        :download = "selectedPar.text"
          :xtitle="selectedPar.text"
          ytitle="Количество ДТП"
          :messages="{ empty: 'Выберите параметр' }"
          :data="parCount"
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
  name: "GraphMonth",
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
    sortDate: function () {
      function date(a, b) {
        if (a < b) return -1;
        if (a > b) return 1;

        return 0;
      }
      return [...this.monthes].sort(date).join(" - "); // shallow clone + sort
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
      if (this.monthes.length == 2) {
        startYM = this.monthes.sort()[0];
        endYM = this.monthes.sort()[1];
        startArr = startYM.split("-");
        endArr = endYM.split("-");
        // console.log(startArr);
        // console.log(endArr);
        startDate = new Date(
          startArr[0],
          startArr[1] - 1,
          1
        ).toLocaleDateString("en-CA");
        endDate = new Date(endArr[0], endArr[1], 0).toLocaleDateString("en-CA");

        // console.log(startDate);
        // console.log(endDate);
      } else if (this.monthes.length == 1) {
        // console.log(endYM);

        startYM = this.monthes.sort()[0];
        startArr = startYM.split("-");
        startDate = new Date(
          startArr[0],
          startArr[1] - 1,
          1
        ).toLocaleDateString("en-CA");
        endDate = new Date(startArr[0], startArr[1], 0).toLocaleDateString(
          "en-CA"
        );

        // console.log(startDate);
        // console.log(endDate);
      }
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
          console.log(url + "&limit=1000000&offset=0");

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
      let key = this.selectedPar.value;
      console.log("key " + key);
      if (!this.selectedTime.value) {
        this.parCount = {}
        for (let i = 0; i < this.items.length; i++) {
          let a = this.items[i][key];
          // var b = Object.keys()
          if (this.parCount[a] != undefined) ++this.parCount[a];
          else this.parCount[a] = 1;
          //    console.log(a)

          // }
        }
      }
      else{
        this.parCount = []
        this.parCountNight={}, this.parCountMorning={}, this.parCountDay={}, this.parCountEvening = {}
        for (let i = 0; i < this.items.length; i++) {
          if(this.items[i]['time']>="00:00:00" && this.items[i]['time']<= "05:59:00"){
            let a = this.items[i][key];
            // var b = Object.keys()
           if (this.parCountNight[a] != undefined) ++this.parCountNight[a];
            else this.parCountNight[a] = 1;
          }
          else if(this.items[i]['time']>="06:00:00" && this.items[i]['time']<= "11:59:00"){
            let a = this.items[i][key];
            // var b = Object.keys()
            if (this.parCountMorning[a] != undefined) ++this.parCountMorning[a];
            else this.parCountMorning[a] = 1;
          }
          else if(this.items[i]['time']>="12:00:00" && this.items[i]['time']<= "17:59:00"){
            let a = this.items[i][key];
            // var b = Object.keys()
           if (this.parCountDay[a] != undefined) ++this.parCountDay[a];
            else this.parCountDay[a] = 1;
          }
          else{
            let a = this.items[i][key];
            // var b = Object.keys()
            if (this.parCountEvening[a] != undefined) ++this.parCountEvening[a];
            else this.parCountEvening[a] = 1;
          }
        }
        this.parCount.push({name: 'Ночь', data: this.parCountNight}, {name: 'Утро', data: this.parCountMorning},
        {name: 'День', data: this.parCountDay}, {name: 'Вечер', data: this.parCountEvening},  )
        
      }
      console.log(this.parCount);
    },
  },
  data() {
    return {
      url: "http://127.0.0.1:8000/api/incident/subjects",
      urlD: "http://127.0.0.1:8000/api/incident/districts/?id_subject__id=",
      monthes: ["2015-01", "2015-02"],
      subjects: [],
      selectedSubject: [15],
      types: [],
      selectedType: [],
      items: [],
      item: [],
      elems:[{data: {'0': 509, '1': 116, '2': 17,'3 и выше': 8}, name: 'Ночь'},
      {data: {'0': 1550, '1': 143, '2': 12,'3 и выше': 10}, name: 'Утро'},
      {data: {'0': 2169, '1': 174, '2': 19,'3 и выше': 6}, name: 'День'},
      {data: {'0': 2118, '1': 318, '2': 33,'3 и выше': 5}, name: 'Вечер'}, ],
      options: {},
      totalItems: 0,
      progressBar: false,
      parCount: {},
      parCountNight:{},
      parCountMorning:{},
      parCountDay:{},
      parCountEvening:{},
      
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

      time: [
        { text: "По суткам", value: false },
        { text: "По времени суток", value: true },
      ],
      selectedTime: { text: "По времени суток", value: true },
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
      separate: false,
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
#main_month{
    padding: 1px;
    border: 0.5px lightgray;
    border-style: solid;
    border-radius: 5px;
}

#button {
  width: 100%;
}


.data_container {
  padding: 0px;
}
.container--fluid{
  max-width: 99%;
  margin-top: 10px;
  margin-bottom: 0;
  padding-bottom: 0;
}
.v-text-field.v-text-field--enclosed >>> .v-text-field__details{
    margin-bottom: 0 !important;
}
.v-input__control >>> .v-text-field__details{
    display: none !important;
}
</style>