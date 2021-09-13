<template>
  <div>
    <apexchart class="chart mx-auto" type="line" :options="options" :series="series"></apexchart>
  </div>
</template>

<script>
  export default {
    props: ['x-axis', 'y-axis'],
    data() {
      return {
        }
    },
    computed: {
      options() {
        return {
          chart: {
            id: 'company information',
            toolbar: {
              show: false
            },
          },

          colors: ['#1e88e5', '#ffa726'],
          xaxis: {
            categories: this.xAxis
          },
          grid: {
            show: true,
            borderColor: '#bdbdbd',
            position: 'back',
            xaxis: {
              lines: {
                show: true
              }
            },   
            yaxis: {
              lines: {
                show: true
              }
            },  
            row: {
              colors: undefined,
              opacity: 0.5
            },  
            column: {
              colors: undefined,
              opacity: 0.5
            },
          },
          stroke: {
            curve: 'straight',
          }
        }
      },
      series() {
        return [{
          name: 'Среднегодовая цена акции компании',
          data: this.yAxis
        }]
      }
    }
  }
</script>

<style lang="scss" scoped>
.chart {
  width: 90%;
}
</style>