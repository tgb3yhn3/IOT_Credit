<template>
<Suspense>
  <template #fallback>
    Loading...
  </template>
  <template #default >
   
  <v-card v-if='datas.advice' class="mx-auto" width="1200" style="background-color:#FFF8F6;" >
    
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
      <v-table  height="auto">
        <thead class="thead ">
          <tr>
            <th class="thead"></th>
            <th class="thead">信貸比</th>
            <th class="thead">月支出收入比</th>
            <th class="thead">月收入</th>
          </tr>
        </thead>
        <tbody>
          <tr class="table-top">
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
          <tr class="table-top b">
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
       
          <!-- <div style=" background-color: #fff !important;"></div> -->
          
        </tbody>
      </v-table>
<br>
      <v-row > 
            <v-col
              cols="4"
              v-for="(option, index) in chartOptions"
              :key="index"
              class="CanvasJSChart"
            >
              <CanvasJSChart :options="option" class="" />
            </v-col>
          </v-row>
    </v-card-text>
  </v-card>
 
  </template>
</Suspense>
</template>
<style scoped>

.v-card {
  /* background-color: red; */
}
.v-table{
  overflow: hidden !important;
  margin-top: 4%;
  /* background-color: #FFF; */
  /* border: 1px solid black; */
  border-bottom: 5px solid #AEC5EB;
  border-right: 5px solid #AEC5EB;
  border-radius: 20px;
}

tbody{
  /* font-size:; */
}
th{
  background-color: #d6e4fa !important;
  font-weight:600 !important;

  font-size: 20px;
}
.table-top{
  /* background-color: #d6e4fa; */
  font-size: 20px;
  font-weight: 200;
  font-weight:600;
}
.b {
  border:10px solid black;
}
h2{
  padding: 3%;
  
    text-align: center;
  background-color: #d6e4fa;
  border-bottom: 5px solid #AEC5EB;
  border-right: 5px solid #AEC5EB;
  border-radius: 20px;

}
.CanvasJSChart{
  border: 2px solid #d6e4fa;
  border-radius: 5%;
  background-color: #fff;
  
  /* padding: 0; */
}

.canvasjs-chart-canvas{
  border: 1px solid black;
  border-radius: 50%;
}

</style>
<script>
import axios from 'axios';
import * as CanvasJS from '@canvasjs/charts';
export default {
  data() {
    return {
      datas: this.$store.state.data
    };
  },
  created(){
    CanvasJS.addColorSet("colors1", ["#685044", "#9575CD", "#F9DEC9"]);
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
                    backgroundColor: "#fff",
                    cornerRadius: 4,
                    colorSet: "colors1",
                    data: [{
                        type: "pyramid",
                        
                        dataPoints: [
                            { label: "", y: 100-value, },

                            { label: "你", y: 0 },
                            { label: "", y: value },
                        ]
                    },],
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
