import api from '../_api'

const getQuestions = (context, questionSet) => {
  api.fetchQuestions(questionSet)
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
