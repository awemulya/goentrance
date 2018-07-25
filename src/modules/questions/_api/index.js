import Api from '@/api/Api'

export default {
  fetchQuestions (question_set) {
    let params = {}
    params['question_set'] = question_set
    return Api().get('questions/', {
      params: params
    })
  }
}
