<template>
<Suspense>
  <template #fallback>
    Loading...
  </template>
  <template #default>
   
  <v-card v-if='datas.advice' class="mx-auto" width="1000"  >
    
    <template v-slot:title>  評估建議 </template>
    <v-divider></v-divider>
    <v-card-text>
        <h2 v-if='datas["advice"]["建議借貸金額"][1]!=0'>
            
            建議借貸金額 {{ Math.round(datas["advice"]["建議借貸金額"][0])}}~{{ Math.round(datas["advice"]["建議借貸金額"][1]) }}
        </h2>
        <h2 v-if='datas["advice"]["建議借貸金額"][1]==0'>
            
            不建議借貸 
        </h2>
        <h2 v-if='datas["advice"]["建議"].length!=0'>
            
            <div v-for="(item, index) in datas['advice']['建議']" :key="index">
             {{ item }}
        </div>
            
            
        </h2>
        <h2 v-if='datas["advice"]["不良紀錄"].length!=0'>
            
            <div v-for="(item, index) in datas['advice']['不良紀錄']" :key="index">
             {{ item }}
        </div>
            
        </h2>
      <v-table fixed-header height="auto">
        <thead>
          <tr>
            <th></th>
            <th>信貸比</th>
            <th>月支出收入比</th>
            <th>月收入</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>在所有客戶中排名</td>
            <td :style="getCellStyle(datas['RevolvingUtilization_rank'])">
              {{ datas["RevolvingUtilization_rank"] }} %
            </td>
            <td :style="getCellStyle(datas['DebtRatio_rank'])">
              {{ datas["DebtRatio_rank"] }} %
            </td>
            <td :style="getCellStyle(datas['MonthlyIncome_rank'])">
              {{ datas["MonthlyIncome_rank"] }} %
            </td>
          </tr>
          <tr>
            <td>在所有同齡客戶中排名</td>
            <td
              :style="getCellStyle(datas['same_age_RevolvingUtilization_rank'])"
            >
              {{ datas["same_age_RevolvingUtilization_rank"] }} %
            </td>
            <td :style="getCellStyle(datas['same_age_DebtRatio_rank'])">
              {{ datas["same_age_DebtRatio_rank"] }} %
            </td>
            <td :style="getCellStyle(datas['same_age_MonthlyIncome_rank'])">
              {{ datas["same_age_MonthlyIncome_rank"] }} %
            </td>
          </tr>
          <tr>
            <td colspan="4">
          <v-row > 
            <v-col
              cols="4"
              v-for="(option, index) in chartOptions"
              :key="index"
            >
              <CanvasJSChart :options="option" />
            </v-col>
          </v-row>
        </td>
        </tr>
        </tbody>
      </v-table>

      
    </v-card-text>
  </v-card>
 
  </template>
</Suspense>
</template>
<style scoped>
h2{
    text-align: center;
}
</style>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      datas: this.$store.state.data
    };
  },
  async  mounted() {
    console.log('created');
    console.log(this.$store.state.data.advice==undefined)
    const request=await axios
        .get("http://127.0.0.1:5001/history/last")
        .then((res) => {
          // console.log(res.data);
          // this.$store.commit("Loaded",res.data)
          // this.$store.state.data=res.data
          this.datas=res.data
        })
    console.log(request)

  },
  computed: {
    // datas(){
    //   return  this.$store.state.data 
      
    // },
        chartOptions() {
            const titles = {
                'RevolvingUtilization_rank': '信貸比排名',
                'DebtRatio_rank': '月支出收入比排名',
                'MonthlyIncome_rank': '月收入排名',
                'same_age_RevolvingUtilization_rank': '同齡信貸比排名',
                'same_age_DebtRatio_rank': '同齡月支出收入比排名',
                'same_age_MonthlyIncome_rank': '同齡月收入排名'
            };

            return Object.entries(this.datas)
                .filter(([key, _]) => key !== 'advice')  // 過濾掉 'advice'
                .map(([key, value]) => ({
                    animationEnabled: true,
                    title: {
                        text: titles[key] || key
                    },
                    data: [{
                        type: "pyramid",
                        dataPoints: [
                            { label: "", y: 100-value },

                            { label: "你", y: 0 },
                            { label: "", y: value },
                        ]
                    }]
                }));
        }
    },
  methods: {
    round(number){
        return Math.round(number)
    },
    getCellStyle(percentage) {
      const size = this.calculateFontSize(percentage);
      const color = this.calculateColor(percentage);
      return {
        fontSize: `${size}px`,
        color: color,
      };
    },
    calculateFontSize(percentage) {
      // 根據百分比調整字體大小
      // 這裡的公式可以根據您的需求進行調整
      return 25 + percentage / 5;
    },
    calculateColor(percentage) {
      // 根據百分比從藍色過渡到紅色
      // 這裡的顏色計算邏輯可以根據您的需求進行調整
      const red = Math.min(255, 2 * percentage);
      const blue = Math.max(0, 255 - 2 * percentage);
      return `rgb(${red}, 0, ${blue})`;
    },
  },
};
</script>
