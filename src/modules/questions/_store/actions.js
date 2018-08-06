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

const getSet = (context, questionSet) => {
  api.fetchSet(questionSet)
    .then((response) => {
      context.commit('SET_UPDATED', response.data)
    })
    .catch((error) => {
      // eslint-disable-next-line
      console.error(error);
    })
}

export default {
  getQuestions, getSet
}
