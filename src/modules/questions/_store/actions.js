import api from '../_api'

const getQuestions = (context, question_set) => {
  api.fetchQuestions(question_set)
    .then((response) => {
      context.commit('QUESTION_UPDATED', response.data)
    })
    .catch((error) => {
      // eslint-disable-next-line
      console.error(error);
    })
}

export default {
  getQuestions
}
