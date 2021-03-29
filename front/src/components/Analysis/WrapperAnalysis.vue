<template>
  <v-app>
  <v-container fluid>
    <v-main>
    <TypicalViolator/>
    </v-main>
  </v-container>
  </v-app>
</template>

<script>
import axios from "axios";
import TypicalViolator from "@/components/Analysis/TypicalViolator"
// import Chart from "chart.js";

// import Header from "@/components/Header";

// import { yandexMap, ymapMarker , loadYmap} from "vue-yandex-maps";
export default {
  name: "Main",
  components: {
    TypicalViolator
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

.container {
  padding-left: 0px;
  padding-right: 0px;
}

</style>
