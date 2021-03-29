<template>
  <v-container fluid>
    <v-main>
      <v-container fluid>
        <v-row>
          <v-select
            v-model="selectedItem"
            solo
            label="Выбор сущности"
            :items="groups"
            item-text="text"
            item-value="value"
            return-object
                              color="green lighten-1"

            
          />
          <v-select
          v-model="selectedTable"
                              color="green lighten-1"

            label="Выбор таблицы"
            solo
            :items="tables.filter(i => i.parent === selectedItem.value)"
            item-text="text"
            item-value="value"
            @change="createUrl"       
            return-object

          />
        </v-row>
      </v-container>
      <VuetifyDatatable :url="url" />
    </v-main>
  </v-container>
</template>

<script>
// import Vue from 'vue'
import VuetifyDatatable from "@/components/ViewAllData/VuetifyDatatable";

export default {
  name: "WrapperData",

  components: {
    VuetifyDatatable,
  },
  methods: {
    createUrl() {
      console.log(this.selectedItem.value)
      this.url='http://127.0.0.1:8000/api/'+this.selectedItem.value+"/"+this.selectedTable.value;
      console.log("___"+this.url)
      return this.url;
    }
  },
  data() {
    return {
      
      url:'http://127.0.0.1:8000/api/transport/transports',
      groups: [
        { text: "Транспорт", value: "transport" },
        { text: "Участник", value: "participant" },
        { text: "Происшествие", value: "incident" },
      ],
      selectedItem: { text: "Транспорт", value: "transport" },
      selectedTable: { text: "Транспортные средства", value: "transports" },
      tables: [
        { text: "Совершаемые действия", value: "transportactions", parent:"transport" },
        { text: "Цвета", value: "colors", parent:"transport" },
        { text: "Типы ТС", value: "transporttypes",parent:"transport"  },
        { text: "Транспортные средства", value: "transports", parent:"transport" },
        { text: "Типы привода", value: "drivetypes", parent:"transport" },
        { text: "Технические неисправности", value: "technicalissues", parent:"transport" },
        { text: "Виды владения", value: "ownershiptypes",parent:"transport"  },
        { text: "Производители", value: "brands", parent:"transport" },
        { text: "Модели", value: "models", parent:"transport" },

        { text: "Категории участников", value: "participantcategories", parent:"participant" },
        { text: "Последствия", value: "consiquences", parent:"participant" },
        { text: "Действия участников", value: "participantactions",parent:"participant"  },
        { text: "Нарушения", value: "violations", parent:"participant" },
        { text: "Участники", value: "participants", parent:"participant" },
        
        { text: "Субъекты", value: "subjects", parent:"incident" },
        { text: "Районы", value: "districts",parent:"incident"  },
        { text: "Населенные пункты", value: "localities", parent:"incident" },
        { text: "Дороги", value: "roads", parent:"incident" },
        { text: "Категории улиц", value: "streetcategories", parent:"incident" },
        { text: "Значения дорог", value: "roadimportances",parent:"incident"  },
        { text: "Адреса", value: "addresses", parent:"incident" },
        { text: "Объекты", value: "objects", parent:"incident" },
        { text: "Виды просишествий", value: "incidenttypes", parent:"incident" },
        { text: "Погодные условия", value: "weathers",parent:"incident"  },
        { text: "Состояние дорожного покрытия", value: "roadwaystatuses", parent:"incident" },
        { text: "Освещение", value: "lightings", parent:"incident" },
        { text: "Изменения в движении", value: "drivingchanges",parent:"incident"  },
        { text: "Причины происшествий", value: "influencefactors", parent:"incident" },
        { text: "Недостатки дорожного покрытия", value: "roaddisadvantages", parent:"incident" },
        
      ],
    }
  },
  watch: {
  },
  beforeCreate(){
  },
  created(){
      
    },
  mounted() {
    
    this.createUrl()

  },
  updated() {
  },
};
</script>

<style scoped> 
*{
  font-family: "Ubuntu", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
#app {
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
.v-select{
  margin-left: 2%;
  margin-right: 2%;
  width: 20rem;
  font-size: large;

}
.text-start{
  font-size: 42px;
}
.v-data-table-header th {
  white-space: nowrap;
}
</style>
