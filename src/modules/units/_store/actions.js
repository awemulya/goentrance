import api from '../_api'

const getUnits = (context, subject) => {
  api.fetchUnits(subject)
    .then((response) => {
      context.commit('UNITS_UPDATED', response.data)
    })
    .catch((error) => {
      // eslint-disable-next-line
      console.error(error);
    })
}

export default {
  getUnits
}
