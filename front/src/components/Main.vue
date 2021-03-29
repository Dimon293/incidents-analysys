<template>
  <v-app>
    <v-container fluid>
      <v-main>
        <v-container fluid>
          <v-row id="first">
            <v-col lg="3" sm="4" cols="12" class="pa-1 ma-0"
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
            <v-col lg="1" sm="2" cols="12" class="pa-1 ma-0"
              ><v-select
                id="day"
                color="green"
                outlined
                item-color="green"
                dense
                height="45px"
                @change="generateUrl"
                v-model="selectedTime"
                label="Время"
                :items="time"
                item-text="text"
                return-object
            /></v-col>

            <v-col lg="3" sm="6" cols="12" class="pa-1 ma-0"
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
            <v-col lg="2" sm="6" cols="12" class="pa-1 ma-0"
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

            <v-col lg="3" sm="6" cols="12" class="pa-1 ma-0"
              ><v-select
                @change="generateUrl"
                v-model="selectedType"
                label="Типы происшествий"
                color="green"
                height="45px"
                item-color="green"
                dense
                outlined
                :items="sortTypes"
                item-text="value"
                item-value="id"
                multiple
                chips
              >
                <template v-slot:selection="{ item, index }">
                  <v-chip v-if="index === 0" small>
                    <span>{{ item.value }}</span>
                  </v-chip>
                  <span v-if="index === 1" class="grey--text caption">
                    (+{{ selectedType.length - 1 }} других)
                  </span>
                </template>
              </v-select></v-col
            >
          </v-row>
          <!-- <v-row>
            <v-col>
              <v-btn
  elevation="2"
  outlined
  plain
                 color="green"
                 ma-10
>Загрузить фотографию </v-btn>
            </v-col>
            <v-col>
            </v-col>
            <v-col>
            </v-col>
          </v-row> -->
        </v-container>

        <!-- <template color>
          <v-app>
            <v-card width="400" class="mx-auto mt-5">
              <v-card-title class="pb-0 mb-4 text-center ">
                <h1 class="text-center">Авторизация</h1>
              </v-card-title>
              <v-card-text >
                <v-form  color="success">
                  <v-select  color="success"
                    :items='users'
                    prepend-icon="mdi-account-circle"
                  />
                  <v-text-field  color="success"
                    :type="showPassword ? 'text' : 'password'"
                    label="Пароль"
                    prepend-icon="mdi-lock"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    @click:append="showPassword = !showPassword"
                  />
                </v-form>
              </v-card-text>
              <v-divider></v-divider>
              <v-card-actions>
                <v-btn color="success">Авторизация</v-btn>
              </v-card-actions>
            </v-card>
          </v-app>
        </template> -->


        <YaMap :items="items" />

        <v-container fluid class="data_container">
          <v-layout column>
            <v-flex md6 style="overflow: auto">
              <v-app>
                <v-data-table
                  loading-text="Укажите дату и регион"
                  no-data-text="Объекты не обнаружены"
                  :headers="headers"
                  :items="items"
                  :options.sync="options"
                  :server-items-length="totalItems"
                  class="elevation-1"
                  multi-sort
                  loading="true"
                  :footer-props="{
                    itemsPerPageOptions: [50],
                    showFirstLastPage: true,
                    firstIcon: 'mdi-arrow-collapse-left',
                    lastIcon: 'mdi-arrow-collapse-right',
                    prevIcon: 'mdi-minus',
                    nextIcon: 'mdi-plus',
                  }"
                  @click:row="showInfoDialog"
                  ><v-progress-linear
                    v-show="progressBar"
                    slot="progress"
                    color="green"
                    indeterminate
                  ></v-progress-linear>
                  <template v-slot:[`item.deaths`]="{ item }">
                    <v-chip :color="getColor(item.deaths)" dark>
                      {{ item.deaths }}
                    </v-chip>
                  </template>
                  <template v-slot:[`item.wounds`]="{ item }">
                    <v-chip :color="getColor(item.wounds)" dark>
                      {{ item.wounds }}
                    </v-chip>
                  </template>
                  <template v-slot:[`item.id`]="{  }">
                    <v-icon small class="mr-2" >
                      mdi-pencil
                    </v-icon>
                    <v-icon small>
                      mdi-delete
                    </v-icon>
                  </template>
                </v-data-table>
              </v-app>
            </v-flex>
          </v-layout>
        </v-container>
        <template>
  <v-dialog v-model="dialog" width="80vw">
    <v-card>
      <v-card-title class="headline">
        Подробные сведения о происшествии
      </v-card-title>
      <json-viewer :value="item" rootKey="Происшествие" />
      <v-btn color="red darken-4" text @click="showInfoDialog"> Закрыть </v-btn>
    </v-card>
  </v-dialog>
</template>
      </v-main>
    </v-container>
  </v-app>
</template>

<script>
import axios from "axios";
// import Header from "@/components/Header";
// import { JSONView } from "vue-json-component";
import JsonViewer from "vue-json-viewer";

import YaMap from "@/components/Map/YaMap";

// import { yandexMap, ymapMarker , loadYmap} from "vue-yandex-maps";
export default {
  name: "Main",
  components: { JsonViewer, YaMap },
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
    sortTypes: function () {
      function f(a, b) {
        if (a.value < b.value) return -1;
        if (a.value > b.value) return 1;
        return 0;
      }
      return [...this.types].sort(f); // shallow clone + sort
    },
  },

  methods: {
    getColor(par) {
      if (par > 3) return "red";
      else if (par > 0) return "orange";
      else return "green";
    },
    showInfoDialog(id) {
      if (this.dialog == false) {
        this.dialog = true;
        this.readOneItemFromAPI(
          "http://127.0.0.1:8000/api/incident/incidentsD/" + id.id
        );
      } else this.dialog = false;
    },
    readOneItemFromAPI(url) {
      // console.log(this.options);
      axios
        .get(url)

        .then((response) => {
          //Then injecting the result to datatable parameters.
          this.item = response.data;
          // var i = response.data;
          console.log(this.item);
          // this.headers = this.getHeaders(this.items[0]);
        });
    },

    // getArrOfValues(arr, attributeName) {
    //   return arr
    //     .filter(function (obj) {
    //       if (attributeName in obj) {
    //         return true;
    //       } else {
    //         return false;
    //       }
    //     })
    //     .map(function (obj) {
    //       return obj[attributeName];
    //     })
    //     .sort();
    // },
    generateUrl() {
      this.url = "http://127.0.0.1:8000/api/incident/incidentsT/?";
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
        "&start_time=" +
        this.selectedTime.start +
        "&end_time=" +
        this.selectedTime.end +
        "&id_address__id_road__id_locality__id_district=" +
        this.selectedDistrict.join() +
        "&id_type=" +
        this.selectedType.join();
      console.log("Url");
      console.log(this.url);
      this.readDataFromAPI(this.url);
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
            itemsPerPage +
            "&offset=" +
            pageNumber * itemsPerPage
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
          console.log("items");
          console.log(this.items);
          console.log(
            url +
              "&ordering=" +
              sortIn +
              "&limit=" +
              itemsPerPage +
              "&offset=" +
              pageNumber * itemsPerPage
          );

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
          console.log("SUBJ");
          console.log(this.subjects);
        });
    },
    getDistricts(subjects) {
      console.log(subjects);
      axios
        .get(this.urlD + subjects.join() + "&limit=" + 100 + "&offset=" + 0)
        .then((response) => {
          this.districts = response.data.results;
        });
      console.log(this.districts);
    },
    getTypes() {
      axios
        .get(this.urlType + "/?limit=" + 30 + "&offset=" + 0)
        .then((response) => {
          this.types = response.data.results;
          this.selectedType = this.types.map((a) => a.id);
        });
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
  },
  data() {
    return {
      url: "http://127.0.0.1:8000/api/incident/subjects",
      urlD: "http://127.0.0.1:8000/api/incident/districts/?id_subject__id=",
      urlType: "http://127.0.0.1:8000/api/incident/incidenttypes",
      monthes: ["2020-10", "2020-11"],
      subjects: [],
      selectedSubject: [15],
      districts: [],
      selectedDistrict: [15401],
      types: [],
      selectedType: [],
      items: [],
      item: [],
      options: {},
      totalItems: 0,
      progressBar: false,
      time: [
        { text: "Сутки", start: "0:00", end: "23:59" },
        { text: "Утро", start: "6:00", end: "12:00" },
        { text: "День", start: "12:00", end: "18:00" },
        { text: "Вечер", start: "18:00", end: "23:59" },
        { text: "Ночь", start: "00:00", end: "6:00" },
      ],
      selectedTime: { text: "Сутки", start: "0:00", end: "23:59" },
      headers: [
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

        { text: "", value: "id" },
      ],
        users:["Администратор", "Пользователь"],
      menu: false,
      modal: false,
      dialog: false,
      coords: [],
    };
  },
  watch: {
    items() {
      this.progressBar = false;
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
        console.log("districts");
        console.log(this.districts);
        console.log("DO");
        console.log(this.selectedDistrict);

        let districtsId = this.districts.map((a) => a.id);
        console.log(districtsId);

        for (let i = 0; i < this.selectedDistrict.length; i++) {
          if (!districtsId.includes(this.selectedDistrict[i])) {
            console.log(this.selectedDistrict[i]);
            this.selectedDistrict.splice(i, 1);
          }
        }

        // for (var i = 0; i < this.selectedDistrict.length; i++) {
        //   console.log("I");
        //   console.log(this.selectedDistrict[i]);

        //   if (this.districts["id"].indexOf(this.selectedDistrict[i]) != -1) {
        //     // this.selectedDistrict.splice(i, 1);

        //     console.log("IF");
        //     console.log(this.selectedDistrict[i]);
        //   }
        // }
      },

      deep: true,
    },
  },
  beforeCreate() {},
  created() {
    this.getSubjects();
    this.getTypes();
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
/* #app {
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
} */

#first .v-col {
  padding: 4%;
}
#button {
  width: 100%;
}

.v-data-table {
}
.data_container {
  padding: 0px;
}
.v-data-table-header th {
  white-space: nowrap;
}
/* .v-date-picker {
  font-size: small;
} */
.container {
  padding-bottom: 0;
}

.v-application--is-ltr >>> .v-data-table {
  vertical-align: center !important;
}

.v-data-table-header th {
  white-space: nowrap;
  vertical-align: top;
}
.text-start {
  font-size: small !important;
}
.v-application >>> .text-start {
  text-align: center !important;
  padding: 2px;
}
.v-dialog__content >>> .v-dialog {
  min-width: fit-content !important;
  max-width: 90vw !important;
}
.json-view-item {
  text-align: left;
  font-size: small;
}
.card {
  width: 30%;
  height: 50vh;
}
.json-view-item >>> .value-key {
  white-space: inherit !important;
}
.ymap-container {
  height: 100%;
}
.v-text-field.v-text-field--enclosed >>> .v-text-field__details {
  margin-bottom: 0 !important;
}
.v-input__control >>> .v-text-field__details {
  display: none !important;
}
.v-data-table th {
  font-size: 40px;
}

.v-data-table td {
  font-size: 40px;
}
</style>