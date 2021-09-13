import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import VueApexCharts from 'vue-apexcharts'
import Vuetify from 'vuetify'
import colors from 'vuetify/es5/util/colors'

Vue.use(VueApexCharts)
Vue.component('apexchart', VueApexCharts)
Vue.use(Vuetify, {
  theme: {
    primary: colors.blue.darken4,
    secondary: colors.amber.lighten2
  }
})


Vue.config.productionTip

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
