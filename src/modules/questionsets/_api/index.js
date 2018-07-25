import Api from '@/api/Api'

export default {
  fetchQuestionSets (chapter) {
    let params = {}
    params['chapter'] = chapter
    return Api().get('question-sets/', {
      params: params
    })
  }
}
