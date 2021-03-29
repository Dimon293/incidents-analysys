<template>
  <div id="bal">
    <p><strong>Тип происшествия:</strong> {{ marker.type }}</p>
    <p><strong>Дата и время:</strong> {{ marker.date }} {{ marker.time }}</p>
    <p><strong>Участники:</strong> {{ marker.p_count }}</p>
    <p><strong>Транспортные средства:</strong> {{ marker.t_count }}</p>
    <p><strong>Пострадавшие:</strong> {{ marker.wounds }}</p>
    <p><strong>Погибшие:</strong> {{ marker.deaths }}</p>
    <v-btn id="btn">Полные сведения</v-btn>
    
  </div>
</template>
<script>
import axios from "axios";
export default {
  props: ["marker"],
  data() {
    return {
      dialog: false,
      item: []
    };
  },
  methods: {
    showInfoDialog() {
      if (this.dialog == false) {
        this.dialog = true;
        this.readOneItemFromAPI(
          "http://127.0.0.1:8000/api/incident/incidentsD/" + this.marker.id
        );
      } else this.dialog = false;
    },
    readOneItemFromAPI(url) {
      axios
        .get(url)

        .then((response) => {
          this.item = response.data;
          console.log(this.item);
        });
    },
  },
};
</script>
<style scoped>
#bal {
  padding: 0.5rem;
  line-height: 0.3rem;
}
</style>