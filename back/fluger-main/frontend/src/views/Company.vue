<template>
  <div class="company">
    <v-card class="my-6">
      <v-simple-table>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center">
                Годы
              </th>
              <th class="text-center">
                Цены
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              :key="obj.year"
              v-for="obj in predictionsData"
            >
              <td class="text-center">{{ obj.year }}</td>
              <td class="text-center">{{ obj.price.toFixed(2) }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-card>
    <v-btn
      color="primary"
      large
      tile
      @click="showChart = !showChart"
      class="my-6 mx-auto d-block"
    >{{ showChart ? 'Скрыть' : 'Показать' }} график</v-btn>
    <chart v-if="showChart" :x-axis="years" :y-axis="prices"/>
  </div>
</template>

<script>
import chart from "../components/Chart.vue"

export default {
  components: {
    chart
  },
  data() {
    return {
      name: '',
      metaInfo: {},
      predictionsData: [
        {
          year: 2021,
          price: 617.0901875
        },
        {
          year: 2022,
          price: 656.3474277
        },
        {
          year: 2023,
          price: 695.60466789
        },
        {
          year: 2024,
          price: 734.86190809
        },
        {
          year: 2025,
          price: 774.11914828
        },
      ],
      showChart: false
    }
  },
  created() {
    
  },
  methods: {
    
  },
  computed: {
    years() {
      return this.predictionsData.map(obj => obj.year)
    },
    prices() {
      return this.predictionsData.map(obj => Number(obj.price.toFixed(2)))
    }
  },
}
</script>

<style lang="scss" scoped>

</style>