<template>
  <v-app id="inspire">
    <v-data-table
      :page="page"
      :pageCount="numberOfPages"
      :items-per-page="20"
      :headers="headers"
      :items="items"
      :options.sync="options"
      :server-items-length="totalItems"
      class="elevation-1"
      loading="true"
      

      loading-text="Загрузка данных"
      :footer-props="{
        itemsPerPageOptions:[20],
        showFirstLastPage: true,
        firstIcon: 'mdi-arrow-collapse-left',
        lastIcon: 'mdi-arrow-collapse-right',
        prevIcon: 'mdi-minus',
        nextIcon: 'mdi-plus',
      }"
    >
      <v-progress-linear
        v-show="progressBar"
        slot="progress"
        color="green"
        indeterminate
      ></v-progress-linear>
    </v-data-table>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  name: "VuetifyDatatable",
    props: {
    url:{
      type: String, 
      default: 'http://127.0.0.1:8000/api/transport/transports'
    }, 
  },
  data() {
    return {
      page: 1,
      totalItems: 0,
      numberOfPages: 0,
      progressBar: true,
      items: [],
      options: {},
    };
  },
  //this one will populate new data set when user changes current page.
 
  methods: {
    //Reading data from API method.
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
            "?ordering=" +
            sortIn.join() +
            "&limit=" +
            itemsPerPage +
            "&offset=" +
            pageNumber * itemsPerPage
        )
        .then((response) => {
          //Then injecting the result to datatable parameters.
          this.items = response.data.results;

          this.totalItems = response.data.count;
          this.numberOfPages = Math.ceil(this.totalItems / itemsPerPage);
          this.progressBar = false;
          this.headers = this.getHeaders(this.items[0]);
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

      console.log(this.headers)

      return this.headers;

    },
    
  },
   watch: {
    
      url:'readDataFromAPI' ,
    
    // options: {
    //   handler() {
    //     this.readDataFromAPI(this.url);
    //   },
    // },

    items() {
      this.progressBar = false;
    },
    options: {
      handler() {
        this.readDataFromAPI(this.url);
      },
    },
    deep: true,
  },

};
</script>

<style scoped>
</style>