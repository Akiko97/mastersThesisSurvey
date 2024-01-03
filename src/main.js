import { createApp } from 'vue'
import App from './App.vue'
import { surveyPlugin } from 'survey-vue3-ui'
import ElementPlus from 'element-plus'

import './style.css'
import 'survey-core/defaultV2.min.css'
import 'element-plus/dist/index.css'

createApp(App)
  .use(surveyPlugin)
  .use(ElementPlus)
  .mount('#app')
