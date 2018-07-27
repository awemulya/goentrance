import api from '../_api'

const getQuestionSets = (context, chapter) => {
  api.fetchQuestionSets(chapter)
    .then((response) => {
      context.commit('QUESTION_SETS_UPDATED', response.data)
    })
    .catch((error) => {
      // eslint-disable-next-line
      console.error(error);
    })
}

export default {
  getQuestionSets
}
