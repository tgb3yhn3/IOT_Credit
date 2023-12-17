<template>
    <v-card class="mx-auto" max-width="1200" style="background-color:#FFF8F6;">
        <!-- <v-system-bar
        color="indigo darken-2"
        dark
      >
        <v-spacer></v-spacer>
  
        <v-icon icon="mdi-window-minimize"></v-icon>
  
        <v-icon icon="mdi-window-maximize"></v-icon>
  
        <v-icon icon="mdi-close"></v-icon>
      </v-system-bar>
  
      <v-toolbar
        color="indigo"
        dark
      >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
  
        <v-toolbar-title>Discover</v-toolbar-title>
  
        <v-spacer></v-spacer>
  
        <v-btn icon="mdi-magnify"></v-btn>
      </v-toolbar> -->

        <v-container fluid>
            <v-row dense>
                <v-col v-for="card in  cards " :key="card.title" :cols="card.flex" :variant="elevated">
                    <RouterLink :to="card.link">
                        <v-card  >
                            <v-img :src=card.src class="align-end" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                                height="300px" cover>
                                <v-card-title  class="text-white" v-text="card.title" ></v-card-title>
                            </v-img>


                        </v-card>
                    </RouterLink>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>
  
<script>
import report_img from '@/assets/report.jpg'
import advise_img from '@/assets/advise.jpg'
import credit_img from '@/assets/credit.jpg'
export default {
    data: () => ({
        cards: [
            {
                title: '信用評估',
                src: credit_img,
                flex: 12,
                link: '/credit',
                
            },
            {
                title: '評估建議',
                src: advise_img,
                flex: 8,
                link: '/advise',
            },
            {
                title: '歷史資料',
                src: report_img,
                flex: 4,
                link: '/report',
            },
        ],
    }),
    methods: {
        getImagePath: function (filename) {
            return require('../../assets/' + filename);
        }
    }
}
</script>
  