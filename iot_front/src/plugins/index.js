/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify'
import router from '../router'
import store from '../store'
import CanvasJSChart from '@canvasjs/vue-charts';
    
export function registerPlugins (app) {
  app
    .use(vuetify)
    .use(router)
    .use(store)
    .use( CanvasJSChart)
}
