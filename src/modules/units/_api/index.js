import Api from '@/api/Api'

export default {
  fetchUnits (subject) {
    let params = {}
    params['subject'] = subject
    return Api().get('units/', {
      params: params
    })
  }
}
