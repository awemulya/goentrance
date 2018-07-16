import Api from '@/api/Api'

export default {
  fetchCourses () {
    return Api().get('courses/')
  }
}
