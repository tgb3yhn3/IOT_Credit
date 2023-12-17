<template>
  <v-card class="mx-auto" width="700">
    <template v-slot:title> 信用評分系統 </template>
    <v-divider></v-divider>
    <v-card-text>
      <v-form v-model="valid" @submit.prevent="submitForm" >
        <v-container>
          <v-row>
            <v-col cols="6" md="6">
              <v-text-field
                v-model="credit_ratio"
                label="信貸比"
                required
                
              ></v-text-field>
            </v-col>
            <!-- </v-row>
          <v-row> -->
            <v-col cols="6" md="6">
              <v-text-field
                v-model="age"
                label="年齡"
                required
                
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
              <v-text-field
                v-model="past_30_59"
                label="過去兩年,逾期還款30~59天數"
                required
                
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="6" md="6">
              <v-text-field
                v-model="income_ratio"
                label="月支出收入比"
                required
                
              ></v-text-field>
            </v-col>

            <v-col cols="6" md="6">
              <v-text-field
                v-model="income"
                label="月收入"
                required
                
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
         
              <v-text-field
                v-model="current_credit_loan_case"
                label="當前信用貸款案件量"
                required
                
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
         
              <v-text-field
                v-model="past_90"
                label="過去兩年逾期還款天數90天以上次數"
                required
                
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
         
              <v-text-field
                v-model="current_mortgage_caseload"
                label="當前抵押貸款案件量"
                required
                
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
         
              <v-text-field
                v-model="past_60_89"
                label="過去兩年逾期還款60~89天次數"
                required
                
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
         
              <v-text-field
                v-model="famliy_member_num"
                label="家庭成員數量(不包括自己)"
                required
                
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
        <v-btn type="submit" block class="mt-2" >Submit</v-btn>
      </v-form>
    </v-card-text>
  </v-card>
</template>
  
  <script>
  import axios from 'axios';
export default {
  data: () => ({
    credit_ratio: null,
        age: null,
        past_30_59: null,
        income_ratio: null,
        income:null,
        current_credit_loan_case: null,
        past_90: null,
        current_mortgage_caseload: null,
        past_60_89: null,
        famliy_member_num: null,
  }),
  methods: {
    submitForm: function () {
      
      console.log("send_form");
      var data = {
        credit_ratio: this.credit_ratio,
        age: this.age,
        past_30_59: this.past_30_59,
        income_ratio: this.income_ratio,
        income: this.income,
        current_credit_loan_case: this.current_credit_loan_case,
        past_90: this.past_90,
        current_mortgage_caseload: this.current_mortgage_caseload,
        past_60_89: this.past_60_89,
        famliy_member_num: this.famliy_member_num,
      };
      console.log(data);
      axios
        .post("http://127.0.0.1:5001/credit", data)
        .then((res) => {
          console.log(res.data);
          this.$store.commit("Loaded",res.data)
         
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
        })
        
    },
  },
};
</script>