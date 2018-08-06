const QUESTION_UPDATED = (state, questions) => {
  state.questions = questions
}
const SET_UPDATED = (state, set) => {
  state.set = set
}

export default {
  QUESTION_UPDATED, SET_UPDATED
}
