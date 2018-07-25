import Vue from 'vue'
import Router from 'vue-router'
import HomeView from '@/views/Home'
import SubjectView from '@/views/Subject'
import UnitView from '@/views/Unit'

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
    },
    {
      path: '/unit/:subjectId',
      name: 'Unit',
      component: UnitView
    },
    {
      path: '/question/:chapterId',
      name: 'Chapter',
      component: UnitView
    }
  ]
})
