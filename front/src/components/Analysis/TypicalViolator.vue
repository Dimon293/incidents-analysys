<template>
  <v-app>
    <v-container fluid>
      <v-main>
        <v-container fluid>
          <v-row id="first">
            <v-col lg="4" sm="4" cols="12" class=" pa-1 ma-0"
              ><v-select
                @change="generateUrl"
                v-model="selectedSubject"
                label="Субъект(ы)"
                color="green"
                height="45px"
                item-color="green"
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
              </v-select></v-col
            >
            <v-col lg="4" sm="4" cols="12" class=" pa-1 ma-0"
              ><v-select
                @change="generateUrl"
                v-model="selectedDistrict"
                label="Район(ы)"
                color="green"
                height="45px"
                item-color="green"
                outlined
                :items="sortDistricts"
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
                    (+{{ selectedDistrict.length - 1 }} других)
                  </span>
                </template>
              </v-select></v-col
            >
            <v-col lg="4" sm="4" cols="12" class=" pa-1 ma-0"
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
                    color="green"
                    height="45px"
                    dense
                    outlined
                    item-color="green"
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
                  color="green lighten-1"
                  min="2015-01"
                  max="2020-11"
                  scrollable
                  locale="ru"
                  full-width
                  no-title
                >
                </v-date-picker> </v-menu
            ></v-col>
          </v-row>
        </v-container>

        <v-container fluid class="data_container">
          <v-layout column>
           
                  <v-row>
                    <v-col lg="6" md="6" sm="6" cols="12" class="wrap_graph">
                    <h4 justify="center" class="font-weight-light">Опыт вождения, лет</h4>
                    <pie-chart
                      v-if="!progressBar"
                      :messages="{ empty: 'Нет данных' }"
                      :data="getDrivingExp()"
                    >
                    </pie-chart>
                  </v-col>
                    <v-col lg="6" md="6" sm="6" cols="12" class="wrap_graph">
                    <h4 justify="center" class="font-weight-light">Тип ТС</h4>

                    <pie-chart
                      v-if="!progressBar"
                      :messages="{ empty: 'Нет данных' }"
                      :data="getTransportType()"

                    >
                    </pie-chart>
                  </v-col><v-col lg="6" md="6" sm="6" cols="12" class="wrap_graph">
                    <h4 justify="center" class="font-weight-light">Нарушения</h4>
                    <pie-chart
                      v-if="!progressBar"
                      :messages="{ empty: 'Нет данных' }"
                      :data="getViolation()"
                    >
                    </pie-chart>
                  </v-col>
                  <v-col lg="6" md="6" sm="6" cols="12" class="wrap_graph">
                    <h4 justify="center" class="font-weight-light">Год производства ТС</h4>
                    <bar-chart
                      v-if="!progressBar"
                      :messages="{ empty: 'Нет данных' }"
                      :data="getTransportYear()"
                    >
                    </bar-chart>
                  </v-col>
                  <!-- <v-col lg="4" md="4" sm="6" cols="12" class="wrap_graph">
                    <h4 justify="center" class="font-weight-light">Пол</h4>
                    <bar-chart
                      v-if="!progressBar"
                      :messages="{ empty: 'Нет данных' }"
                      tooltip=true
                      :data="getSex()"
                    >
                    </bar-chart>
                  </v-col> -->
                  <!-- <v-col lg="4" md="4" sm="6" cols="12" class="wrap_graph wrap_graph">
                    <h4 justify="center" class="font-weight-light">Производитель ТС</h4>
                    <bar-chart
                      v-if="!progressBar"
                      :messages="{ empty: 'Нет данных' }"
                      :data="getBrand()"
                    >
                    </bar-chart>
                  </v-col> -->
                  </v-row>
                   <v-flex md6 style="overflow: auto">
              <v-app>
                <v-data-table
                    loading-text="Укажите дату и регион"
                  no-data-text="Объекты не обнаружены"
                  :headers="headers"
                  :items="items"
                  :options.sync="options"
                  :server-items-length="totalItems"
                  class="elevation-1 mb-4"
                  multi-sort
                  loading="true"
                  :footer-props="{
                    itemsPerPageOptions: [20],
                    showFirstLastPage: true,
                    firstIcon: 'mdi-arrow-collapse-left',
                    lastIcon: 'mdi-arrow-collapse-right',
                    prevIcon: 'mdi-minus',
                    nextIcon: 'mdi-plus',
                  
                  }"
                  ><v-progress-linear
                    v-show="progressBar"
                    slot="progress"
                    color="green"
                    indeterminate
                  ></v-progress-linear>
                </v-data-table></v-app>
            </v-flex>
          </v-layout>
        </v-container>
      </v-main>
    </v-container>
  </v-app>
</template>

<script>
import axios from "axios";
import Chartkick from "vue-chartkick";

// import Header from "@/components/Header";

// import { yandexMap, ymapMarker , loadYmap} from "vue-yandex-maps";
export default {
  name: "Main",
  components: {},
  computed: {
    sortSubjects: function () {
      function subjectsTitle(a, b) {
        if (a.title < b.title) return -1;
        if (a.title > b.title) return 1;
        return 0;
      }
      return [...this.subjects].sort(subjectsTitle); // shallow clone + sort
    },
    sortDistricts: function () {
      function districtsTitle(a, b) {
        if (a.title < b.title) return -1;
        if (a.title > b.title) return 1;
        return 0;
      }
      return [...this.districts].sort(districtsTitle); // shallow clone + sort
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
    generateUrl() {
      this.url = "http://127.0.0.1:8000/api/analysis/typicalviolator/?";
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
        "&id_district=" +
        this.selectedDistrict.join();
      // console.log("Url");
      // console.log(this.url);
      this.readDataFromAPI(this.url);
      // console.log(this.items)
      // this.getDataFromTable(this.url)
    },
    // console.log(result)

    readDataFromAPI(url) {
      this.progressBar = true;
      // console.log(this.options);
      var { sortBy, sortDesc, page, itemsPerPage } = this.options;
      // console.log(sortBy, sortDesc, sortIn, page, itemsPerPage);

      var sortIn = [];
      for (var i = 0; i < sortBy.length; i++) {
        if (sortDesc[i] == false || sortDesc[i] === undefined)
          sortIn.push(sortBy[i]);
        else sortIn.push("-" + sortBy[i]);
      }

      let pageNumber = page - 1;
      axios
        .get(
          url +
            "&ordering=" +
            sortIn.join() +
            "&limit=" +
            150 +
            "&offset=" +
            1
        )

        .then((response) => {
          //Then injecting the result to datatable parameters.
          this.items = response.data.results;
          // this.coords = [];
          // for (i in this.items) {
          //   this.coords.push([
          //     i.id_address__latitude,
          //     i.id_address__longtitude,
          //   ]);
          // }
          // console.log("items");
          // console.log(this.items);
          // console.log(
          //   url +
          //     "&ordering=" +
          //     sortIn +
          //     "&limit=" +
          //     itemsPerPage +
          //     "&offset=" +
          //     pageNumber * itemsPerPage
          // );

          this.totalItems = response.data.count;
          this.numberOfPages = Math.ceil(this.totalItems / itemsPerPage);
          this.progressBar = false;
          // this.headers = this.getHeaders(this.items[0]);
        });
    },
    getSubjects() {
      axios
        .get(this.url + "/?limit=" + 100 + "&offset=" + 0)
        .then((response) => {
          this.subjects = response.data.results;
          // console.log("SUBJ");
          // console.log(this.subjects);
        });
    },
    getDistricts(subjects) {
      // console.log(subjects);
      axios
        .get(this.urlD + subjects.join() + "&limit=" + 100 + "&offset=" + 0)
        .then((response) => {
          this.districts = response.data.results;
        });
      // console.log(this.districts);
    },
    getHeaders(response) {
      this.headers = [];
      for (let i in response) {
        var obj = { text: i, value: i };
        this.headers.push(obj);
        //   "text: " + "'"+i+"'"+", value: "+ "'"+i+"'");
      }
      // "text: 'id', value: 'id'",

      // console.log(this.headers);

      return this.headers;
    },
    // setPar() {
    // //   {name: 'Workout', data: {'2017-01-01 00:00:00 -0800': 3, '2017-01-02 00:00:00 -0800': 4}},
    //     this.parCount = [];
    //     for (let i = 0; i < this.items.length; i++) {
    //       // var key = this.items[i][par].toString();
    //       var date = this.items[i]["date"];
    //       var index = this.parCount.map((x) => x.name).indexOf(key);

    //       if (index != -1) {
    //           let obj = this.parCount[index]['data'][date]
    //           if(obj != undefined){
    //               this.parCount[index]['data'][date]++

    //           }
    //           else{
    //               this.parCount[index]['data'][date] = 1
    //           }
    //       } else {
    //         this.parCount.push({ name: key, data: { [date]: 1 } });
    //       }
    //     }
    //     this.parCount.sort((a, b) => a.name.localeCompare(b.name));

    //   console.log(this.parCount);
    // },
    getSex() {
      let arr = this.items.map((a) => a.sex).sort();
      let out = {};
      arr.forEach(function (x) {
        out[x] = (out[x] || 0) + 1;
      });
      return out;
    },
    getBrand() {
      let arr = this.items.map((a) => a.id_brand__title).sort();
      let out = {};
      arr.forEach(function (x) {
        out[x] = (out[x] || 0) + 1;
      });
      return out;
    },
    getDrivingExp() {
      let arr = this.items.map((a) => a.drivingExperience).sort();
      let out = {};
      arr.forEach(function (x) {
        out[x] = (out[x] || 0) + 1;
      });
      return out;
    },
    getTransportType() {
      let arr = this.items.map((a) => a.id_transportType__value).sort();
      let out = {};
      arr.forEach(function (x) {
        out[x] = (out[x] || 0) + 1;
      });
      return out;
    },
    getViolation() {
      let arr = this.items.map((a) => a.id_violationImmediate__value).sort();
      let out = {};
      arr.forEach(function (x) {
        out[x] = (out[x] || 0) + 1;
      });
      return out;
    },
    getTransportYear() {
      let arr = this.items.map((a) => a.transportYear).sort();
      let out = {};
      arr.forEach(function (x) {
        out[x] = (out[x] || 0) + 1;
      });
      return out;
    },
    
    // getDriveType() {
    //   let arr = this.items.map((a) => a.id_driveType__value).sort();
    //   let out = {};
    //   arr.forEach(function (x) {
    //     out[x] = (out[x] || 0) + 1;
    //   });
    //   return out;
    // },
  },
  data() {
    return {
      url: "http://127.0.0.1:8000/api/incident/subjects",
      urlD: "http://127.0.0.1:8000/api/incident/districts/?id_subject__id=",
      monthes: ["2020-01", "2020-11"],
      subjects: [],
      selectedSubject: [15],
      districts: [],
      selectedDistrict: [15401],
      drivingExperience: [],
      items: [],
      item: [],
      options: {},
      totalItems: 0,
      progressBar: false,
      headers: [
        {
          text: "Субъект",
          value: "id_district__id_subject__title",
        },
        {
          text: "Район",
          value: "id_district__title",
        },
        { text: "Дата", value: "date" },
        { text: "Пол", value: "sex" },
        { text: "Ремень", value: "belt" },
        { text: "Опыт вождения", value: "drivingExperience" },
        { text: "Тип ТС", value: "id_transportType__value" },
        { text: "Год производства ТС", value: "transportYear" },
        { text: "Производитель ТС", value: "id_brand__title" },
        { text: "Нарушения", value: "id_violationImmediate__value" },
        

      ],
      menu: false,
      coords: [],
    };
  },
  watch: {
    items() {
      this.progressBar = false;
      console.log(this.items)
    },
    options: {
      handler() {
        this.readDataFromAPI(this.url);
      },
    },
    deep: true,
    selectedSubject: {
      handler() {
        this.getDistricts(this.selectedSubject);
      },
      immediate: true,

      deep: true,
    },
    districts: {
      handler() {
        let districtsId = this.districts.map((a) => a.id);
        // console.log(districtsId);

        for (let i = 0; i < this.selectedDistrict.length; i++) {
          if (!districtsId.includes(this.selectedDistrict[i])) {
            // console.log(this.selectedDistrict[i]);
            this.selectedDistrict.splice(i, 1);
          }
        }
      },

      deep: true,
    },
  },
  beforeCreate() {},
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
  margin-top: 15px;
}

.data_container {
  padding: 5px;
}
.v-data-table-header th {
  white-space: nowrap;
}
/* .v-date-picker {
  font-size: small;
} */

.v-application >>> .v-application--wrap{
  min-height: auto !important;
}
.v-application--is-ltr >>> .v-data-table {
  vertical-align: center !important;
}
.text-start {
  font-size: large !important;
}
.v-application >>> .text-start {
  text-align: center !important;
  padding: 2px;
}
.v-data-table-header th {
  white-space: nowrap;
  vertical-align: top;
}
.v-text-field.v-text-field--enclosed >>> .v-text-field__details {
  margin-bottom: 0 !important;
}
.v-input__control >>> .v-text-field__details {
  display: none !important;
}
.wrap_graph{
  width: 30px;
  padding: 1px;
  border: 0.5px lightgray;
  border-style: solid;
  border-radius: 5px;
}
</style>