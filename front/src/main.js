import Vue from 'vue'
import Header from './Header.vue'
// import YaMap from './components/YaMap.vue'

import vuetify from './plugins/vuetify'
import VueRouter from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import router from './router'
import Chartkick from 'vue-chartkick'
import Chart from 'chart.js'

Vue.config.productionTip = false

window.Vue = Vue
Vue.use(VueAxios, axios)
Vue.use(VueRouter)


Vue.use(Chartkick.use(Chart))
Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(Header)
}).$mount('#app')
