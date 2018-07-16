import api from '../_api'

const getCourses = (context) => {
  api.fetchCourses()
    .then((response) => {
      context.commit('COURSES_UPDATED', response.data)
    })
    .catch((error) => {
      // eslint-disable-next-line
      console.error(error);
    })
}

export default {
  getCourses
}
