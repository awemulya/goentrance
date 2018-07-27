import Api from '@/api/Api'

export default {
  fetchQuestions (questionSet) {
    let params = {}
    params['question_set'] = questionSet
    return Api().get('questions/', {
      params: params
    })
  }
}
