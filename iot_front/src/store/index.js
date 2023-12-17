
import Vuex from 'vuex';



// 定義一個新的 Vue Store
const store = new Vuex.Store({
    state: {
      data: {},
    },
    mutations: {
      // 將state設定為參數
      Loaded(state,new_data) {
        // state的isLoading true/false 互轉
        state.data = new_data
      }
    }

})
export default store;