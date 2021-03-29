<template>
  <div id="ya-map">
    <!-- <yandex-map v-if="markers.lentgth==0"  :zoom="10" :settings="settings" :coords="coords" /> -->
    <!-- <template ><button>BTN</button></template> -->
    <yandex-map
      :settings="settings"
      :coords="[markers[0].lat, markers[0].long]"
      :zoom="12"
    >
      <template v-if="!markers.length" />
      <template v-else
        ><ymap-marker
          @balloonopen="bindListener(marker)"
          @balloonclose="unbindListener"
          v-for="marker in markers"
          :key="marker.id"
          :coords="[marker.lat, marker.long]"
          :markerId="marker.id"
          :icon="{
            layout: 'default#image',
            imageHref: marker.url,
            imageSize: [27, 27],
            imageOffset: [0, 0],
          }"
        >
          <Baloon :marker="marker" slot="balloon"> </Baloon>
        </ymap-marker>
        <template>
          <v-dialog v-model="dialog" max-width="80vw">
            <v-card>
              <v-card-title class="headline">
                Подробные сведения о происшествии
              </v-card-title>
              <json-viewer :value="item" rootKey="Происшествие" />
              <v-btn color="red darken-4" text @click="showInfoDialog">
                Закрыть
              </v-btn>
            </v-card>
          </v-dialog>
        </template></template
      >
    </yandex-map>
  </div>
</template>
<script>
import axios from "axios";
import { yandexMap, ymapMarker } from "vue-yandex-maps";
import JsonViewer from 'vue-json-viewer'
import Baloon from "@/components/Map/Baloon";
export default {
  components: { yandexMap, ymapMarker, JsonViewer, Baloon },
  props: {
    items: {
      type: Array,
    },
  },

  methods: {
    bindListener(marker) {
      this.marker = marker;
      document
        .getElementById("btn")
        .addEventListener("click", this.showInfoDialog);
    },
    unbindListener() {
      document
        .getElementById("btn")
        .removeEventListener("click", this.showInfoDialog);
    },
    showInfoDialog() {
      if (this.dialog == false) {
        this.dialog = true;
        this.readOneItemFromAPI(
          "http://127.0.0.1:8000/api/incident/incidentsD/" + this.marker.id
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
          // console.log(this.item);
          // this.headers = this.getHeaders(this.items[0]);
        });
    },
    itemsToMarkers() {
      this.markers.splice(0);
      for (var i = 0; i < this.items.length; i++) {
        var newObject = {};
        let id = this.items[i].id;
        let type = this.items[i].id_type__value;
        let date = this.items[i].date;
        let time = this.items[i].time;
        let p_count = this.items[i].participant__count;
        let t_count = this.items[i].transport__count;
        let wounds = this.items[i].wounds;
        let deaths = this.items[i].deaths;
        let lat = this.items[i].id_address__latitude;
        let long = this.items[i].id_address__longtitude;
        var obj;
        if (
          type == "Наезд на пешехода" ||
          type ==
            "Наезд на лицо, не являющееся участником дорожного движения, осуществляющее несение службы" ||
          type ==
            "Наезд на лицо, не являющееся участником дорожного движения, осуществляющее производство работ" ||
          type ==
            "Наезд на лицо, не являющееся участником дорожного движения, осуществляющее какую-либо другую деятельность" ||
          type == "Наезд на животное"
        ) {
          if (deaths == 0) {
            obj = this.markerIcons.find((obj) => {
              return obj.type == "participant_no_d";
            });
          } else {
            obj = this.markerIcons.find((obj) => {
              return obj.type == "participant_d";
            });
          }
          newObject = {
            id: id,
            type: type,
            date: date,
            time: time,
            wounds: wounds,
            deaths: deaths,
            p_count: p_count,
            t_count: t_count,
            lat: lat,
            long: long,
            url: obj.url,
          };
        } else if (type == "Наезд на велосипедиста") {
          if (deaths == 0) {
            obj = this.markerIcons.find((obj) => {
              return obj.type == "bicycle_no_d";
            });
          } else {
            obj = this.markerIcons.find((obj) => {
              return obj.type == "bicycle_d";
            });
          }
          newObject = {
            id: id,
            type: type,
            date: date,
            time: time,
            wounds: wounds,
            deaths: deaths,
            p_count: p_count,
            t_count: t_count,
            lat: lat,
            long: long,
            url: obj.url,
          };
        } else {
          if (deaths == 0) {
            obj = this.markerIcons.find((obj) => {
              return obj.type == "transport_no_d";
            });
          } else {
            obj = this.markerIcons.find((obj) => {
              return obj.type == "transport_d";
            });
          }
          newObject = {
            id: id,
            type: type,
            date: date,
            time: time,
            wounds: wounds,
            deaths: deaths,
            p_count: p_count,
            t_count: t_count,
            lat: lat,
            long: long,
            url: obj.url,
          };
        }
        this.$set(this.markers, i, newObject);
      }
      // console.log("TrueMarkers");

      // console.log(this.markers);
    },
  },
  data() {
    return {
      pageReady: false,
      settings: {
        apiKey: "c16a6cf1-9185-46f4-b504-0b5c1fbeab30",
        lang: "ru_RU",
        coordorder: "latlong",
        version: "2.1",
      },
      dialog: false,
      coords: [0, 0],
      ncoords: [50, 42],
      item: {},
      markers: [],
      marker: {},
      markerIcons: [
        {
          type: "participant_no_d",
          url: "https://www.flaticon.com/svg/static/icons/svg/594/594846.svg",
        },
        {
          type: "participant_d",
          url: "https://www.flaticon.com/svg/static/icons/svg/594/594580.svg",
        },

        { type: "bicycle_no_d", url: "https://svgshare.com/i/ScN.svg" },
        { type: "bicycle_d", url: "https://svgshare.com/i/Sdt.svg" },

        {
          type: "transport_no_d",
          url: "https://www.flaticon.com/svg/static/icons/svg/595/595005.svg",
        },
        {
          type: "transport_d",
          url: "https://www.flaticon.com/svg/static/icons/svg/594/594739.svg",
        },
      ],
    };
  },
  updated() {
    // this.itemsToMarkers()
  },
  mounted() {
    // this.itemsToMarkers()
  },

  watch: {
    $props: {
      handler() {
        this.itemsToMarkers();
      },
      deep: true,
      immediate: true,
    },
    // markers() {
    //   console.log("Markers");
    //   console.log(this.markers);
    // },
  },
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
.text-start{
  font-size: small !important;
}
.v-application >>> .text-start {
  text-align: center !important;
  padding: 2px;
  
}
.v-dialog__content >>> .v-dialog{
  min-width: fit-content !important;

}
.json-view-item {
  text-align: left;
  font-size: small;
}
.card {
  width: 100%;
  height: 50vh;
}
#ya-map {
  width: 100%;
  height: 50vh;
}
.ymap-container {
  height: 100%;
}
</style>