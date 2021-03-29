<template>
  <v-app>
    <v-bottom-navigation class="d-flex justify-content ma-0">
      <v-btn width="25%" to="/">
        <span>Главная<br> </span>

        <v-icon color="green lighten-1">mdi-home-outline</v-icon>
      </v-btn>
      <v-btn width="20%" to="/data">
        <span>Данные</span>

        <v-icon color="green lighten-1">mdi-database</v-icon>
      </v-btn>
      <v-btn width="25%" to="/graph">
        <span>Статистика</span>

        <v-icon color="green lighten-1">mdi-poll</v-icon>
      </v-btn>
      <v-btn width="25%" to="/violator">
        <span>Портрет<br>нарушителя</span>

        <v-icon color="green lighten-1">mdi-page-next-outline</v-icon>
      </v-btn>
      <v-btn width="20%" to="/importance">
        <span>Факторы<br>влияния</span>

        <v-icon color="green lighten-1">mdi-chart-scatter-plot-hexbin</v-icon>
      </v-btn>
      <v-btn width="25%" to="/dangerous">
        <span ta-center>Опасные<br>участки</span>

        <v-icon color="green lighten-1">mdi-map-marker-alert-outline</v-icon>
      </v-btn>
      <v-btn width="20%" @click="dialog = true">
      <span>Сбор данных</span>

      <v-icon color="green lighten-1">mdi-arrow-down-bold-hexagon-outline</v-icon>
    </v-btn>
    </v-bottom-navigation>
    <div>
      <router-view />
    </div>
    <!-- <v-dialog  v-model="dialog" hide-overlay persistent width="300"  >
      <v-card color="green lighten-1" dark>
        <v-card-text class="text-center">
          Поиск новых происшествий
          <v-progress-linear
            indeterminate
            color="white"
            class="mb-0 mt-3"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialog2" persistent max-width="500" > 
      <v-card>
        <v-card-title class="headline text-no-wrap">
          Загрузить данные за 2020-12, 2021-01?
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="dialog2 = false">
            Отмена
          </v-btn>
          <v-btn color="green darken-1" text @click="dialog2 = false">
            Да
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog> -->
  </v-app>
</template>
<script>
export default {
  data() {
    return {
      dialog: false,
      dialog2: false,
    };
  },
  // watch: {
  //   dialog(val) {
  //     if (!val) return;
  //     setTimeout(() => (this.dialog = false,this.dialog2 = true), 4000);
      
  //   },
  // },
};
</script>
<style scoped>
.parser{
  margin-bottom: 400px;
}
.headline{
  justify-content: center;
  }
.v-bottom-navigation {
  padding: 10px;
}
.v-btn {
  letter-spacing: 0.01rem;
}
.theme--light.v-btn.v-btn--has-bg{
  background-color: white !important;
}
</style>
<style>
* {
  font-family: "Ubuntu", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

}
span{
  text-align: center;
}
</style>