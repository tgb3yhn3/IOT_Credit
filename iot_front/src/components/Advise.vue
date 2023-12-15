<template>
    <v-card class="mx-auto" width="700" prepend-icon="mdi-home">
        <template v-slot:title> 評估建議 </template>
        <v-divider></v-divider>
        <v-card-text>
            <v-table fixed-header height="700px">
                <thead>
                    <tr>
                        <th></th>
                        <th>信貸比</th>
                        <th>月支出收入比</th>
                        <th>月收入</th>
                    </tr>
                </thead>
                <tbody center>

                    <tr>
                        <td>在所有客戶中排名</td>
                        <td>{{ all.credit_ratio }} %</td>
                        <td>{{ all.income_ratio }} %</td>
                        <td>{{ all.income }} %</td>
                    </tr>
                    <tr>
                        <td>在所有同齡客戶中排名</td>
                        <td>{{ same_age.credit_ratio }} %</td>
                        <td>{{ same_age.income_ratio }} %</td>
                        <td>{{ same_age.income }} %</td>
                    </tr>

                </tbody>
            </v-table>
        </v-card-text>
    </v-card>
</template>
  
<script>
export default {
    data() {
        return {
            all: {
                credit_ratio: 50,
                income_ratio: 50,
                income: 50,
            },
            same_age:{
                credit_ratio: 50,
                income_ratio: 50,
                income: 50,
            },

        }
    },
}

</script>