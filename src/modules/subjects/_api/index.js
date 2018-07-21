import Api from '@/api/Api'

export default {
  fetchSubjects (course) {
    return Api().get('subjects/')
  }
}
