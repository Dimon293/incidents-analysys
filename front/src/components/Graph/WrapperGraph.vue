<template>
  <v-app>
    <GraphMonth/>
    <GraphDay/>
    <!-- <v-container fluid>
      <v-main>
        <v-container fluid>
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
                  max="2020-10"
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

            <v-col lg="3" sm="6" cols="6" class="pa-1 ma-0"
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
            <v-col lg="3" sm="6" cols="6" class="pa-1 ma-0"
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
        <area-chart v-if="!progressBar"
        
        :download = "selectedPar.text"
          :xtitle="selectedPar.text"
          ytitle="Количество ДТП"
          :messages="{ empty: 'Выберите параметр' }"
          :data="parCount"
          :colors="['#4CAF50', '#00f2ff', '#67008a', '#db5b00']"
        >
        </area-chart>
      </v-main>
    </v-container> -->
  </v-app>
</template>

<script>
import axios from "axios";
import Chartkick from "vue-chartkick";
import GraphMonth from "@/components/Graph/GraphMonth"
import GraphDay from "@/components/Graph/GraphDay"
// import Chart from "chart.js";

// import Header from "@/components/Header";

// import { yandexMap, ymapMarker , loadYmap} from "vue-yandex-maps";
export default {
  name: "Main",
  components: {
    GraphMonth, GraphDay
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

#button {
  width: 100%;
}

.data_container {
  padding: 0px;
}

</style>