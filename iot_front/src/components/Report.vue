<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12">
        <v-card
          class="mx-auto"
          width="1200"
          style="background-color: #fff8f6; border: "
        >
          <v-card-title>
            <span class="text-h5">歷史資料</span>
          </v-card-title>
          <v-card-text>
            <v-table dense striped class="">
              <thead>
                <tr>
                  <th class="text-center"></th>
                  <!-- 添加文本對齊 -->
                  <th
                    v-for="header in headers"
                    :key="header.value"
                    class="text-left"
                  >
                    {{ header.text }}
                  </th>
                  <th class="text-center"></th>
                  <!-- 添加文本對齊 -->
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in desserts" :key="item.age">
                  <td>
                    <v-btn
                      small
                      color="#d6e4fa"
                      style="font-size: 17px"
                      @click="navigateTo(item.id)"
                      >查看</v-btn
                    >
                  </td>
                  <td>{{ item.credit_ratio }}</td>
                  <td>{{ item.age }}</td>
                  <td>{{ item.past_30_59 }}</td>
                  <td>{{ item.income_ratio }}</td>
                  <td>{{ item.income }}</td>
                  <td>{{ item.current_credit_loan_case }}</td>
                  <td>{{ item.past_90 }}</td>
                  <td>{{ item.current_mortgage_caseload }}</td>
                  <td>{{ item.past_60_89 }}</td>
                  <td>{{ item.famliy_member_num }}</td>
                  <td>
                    <v-btn
                      small
                      color="#d6e4fa"
                      style="font-size: 17px"
                      @click="DELETE(item.id)"
                      >刪除</v-btn
                    >
                  </td>
                </tr>
              </tbody>
            </v-table>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<style scoped>
.v-card {
  /* background-color: red; */
}
.v-table {
  overflow: hidden !important;
  margin-top: 4%;
  /* background-color: #FFF; */
  border: 1px solid #d6e4fa;
  /* border-bottom: 5px solid #AEC5EB;
  border-right: 5px solid #AEC5EB;*/
  border-radius: 20px;
}

tbody {
}
th {
  background-color: #c9deff !important;
  font-weight: 200;
  font-weight: 600;
  font-weight: bolder !important;
}
.table-top {
  /* background-color: #d6e4fa; */
}
.b {
  border: 10px solid black;
}
h2 {
  padding: 3%;

  text-align: center;
  background-color: #d6e4fa;
  border-bottom: 5px solid #aec5eb;
  border-right: 5px solid #aec5eb;
  border-radius: 20px;
  /* font-weight: 200; */
}
.CanvasJSChart {
  border: 1px solid #7b7d7d;
  border-radius: 5%;
  background-color: #d6e4fa;

  /* padding: 0; */
}

.canvasjs-chart-canvas {
  border: 1px solid black;
  border-radius: 50%;
}
</style>
<script>
import axios from "axios";

export default {
  data() {
    return {
      headers: [
        { text: "Credit Ratio", align: "left", value: "credit_ratio" },
        { text: "Age", align: "left", value: "age" },
        {
          text: "Past 30-59 Days Delinquency",
          align: "left",
          value: "past_30_59",
        },
        { text: "Income Ratio", align: "left", value: "income_ratio" },
        { text: "Income", align: "left", value: "income" },
        {
          text: "Current Credit Loan Case",
          align: "left",
          value: "current_credit_loan_case",
        },
        { text: "Past 90 Days Delinquency", align: "left", value: "past_90" },
        {
          text: "Current Mortgage Caseload",
          align: "left",
          value: "current_mortgage_caseload",
        },
        {
          text: "Past 60-89 Days Delinquency",
          align: "left",
          value: "past_60_89",
        },
        {
          text: "Number of Family Members",
          align: "left",
          value: "famliy_member_num",
        },
      ],
      desserts: [],
    };
  },
  mounted() {
    axios
      .get("/api/history")
      .then((response) => {
        this.desserts = response.data.map((item) => {
          let dataObject;
          try {
            dataObject = JSON.parse(item.data.replace(/'/g, '"'));
            dataObject.id = item.id;
            console.log(dataObject);
          } catch (e) {
            console.error("JSON 解析錯誤:", e);
          }
          return dataObject || {};
        });
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    DELETE(id) {
      axios.delete("/api/history/" + id).then((res) => {
        console.log(res.data);
        // this.$store.commit("Loaded",res.data)

        //   query: {
        //     credit_ratio: res.data.credit_ratio,
        //     income_ratio: res.data.income_ratio,
        //     income: res.data.income,
        //     same_age_credit_ratio: res.data.same_age_credit_ratio,
        //     same_age_income_ratio: res.data.same_age_income_ratio,
        //     same_age_income: res.data.same_age_income,
        //   },
        // });

        this.$router.go();
        // location.reload();
      });
    },
    navigateTo(id) {
      axios.get("/api/history/" + id).then((res) => {
        console.log(res.data);
        this.$store.commit("Loaded", res.data);

        // this.$router.push({
        //   path: "/advise",
        //   query: {
        //     credit_ratio: res.data.credit_ratio,
        //     income_ratio: res.data.income_ratio,
        //     income: res.data.income,
        //     same_age_credit_ratio: res.data.same_age_credit_ratio,
        //     same_age_income_ratio: res.data.same_age_income_ratio,
        //     same_age_income: res.data.same_age_income,
        //   },
        // });
        this.$router.push({
          path: "/advise",
        });
      });
      // 這裡實現您的導航邏輯
    },
  },
};
</script>
