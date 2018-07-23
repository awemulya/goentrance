import Api from '@/api/Api'

export default {
  fetchSubjects (course) {
    let params = {}
    params['course'] = course
    return Api().get('subjects/', {
      params: params
    })
  }
}
