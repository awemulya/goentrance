import api from '../_api'

const getSubjects = (context, course) => {
  api.fetchSubjects(course)
    .then((response) => {
      context.commit('SUBJECTS_UPDATED', response.data)
    })
    .catch((error) => {
      // eslint-disable-next-line
      console.error(error);
    })
}

export default {
  getSubjects
}
