<template>
  <v-card class="mx-auto" width="400" prepend-icon="mdi-home">
    <template v-slot:title> 信用評分系統 </template>
    <v-divider></v-divider>
    <v-card-text>
      <v-form v-model="valid">
        <v-container>
          <v-row>
            <v-col cols="6" md="6">
              <v-text-field
                v-model="credit_ratio"
                label="信貸比"
                required
                hide-details
              ></v-text-field>
            </v-col>
            <!-- </v-row>
          <v-row> -->
            <v-col cols="6" md="6">
              <v-text-field
                v-model="age"
                label="年齡"
                required
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
              <v-text-field
                v-model="past_30_59"
                label="過去兩年,逾期還款30~59天數"
                required
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="6" md="6">
              <v-text-field
                v-model="income_ratio"
                label="月支出收入比"
                required
                hide-details
              ></v-text-field>
            </v-col>

            <v-col cols="6" md="6">
              <v-text-field
                v-model="income"
                label="月收入"
                required
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
         
              <v-text-field
                v-model="current_credit_loan_case"
                label="當前信用貸款案件量"
                required
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
         
              <v-text-field
                v-model="past_90"
                label="過去兩年逾期還款天數90天以上次數"
                required
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
         
              <v-text-field
                v-model="current_mortgage_caseload"
                label="當前抵押貸款案件量"
                required
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
         
              <v-text-field
                v-model="past_60_89"
                label="過去兩年逾期還款60~89天次數"
                required
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12">
         
              <v-text-field
                v-model="famliy_member_num"
                label="家庭成員數量(不包括自己)"
                required
                hide-details
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </v-card-text>
  </v-card>
</template>
  
  <script>
export default {
  data: () => ({}),
};
</script>