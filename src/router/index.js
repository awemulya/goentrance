import Vue from 'vue'
import Router from 'vue-router'
import HomeView from '@/views/Home'
import SubjectView from '@/views/Subject'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/subject/:courseId',
      name: 'Subject',
      component: SubjectView
    }
  ]
})
