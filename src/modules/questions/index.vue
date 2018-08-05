<template>
  <QuestionList :questions="questions" :set="set" />
</template>

<script>
import { mapGetters } from 'vuex'
import store from './_store'
import QuestionList from './_components/QuestionList'

export default {
  name: 'QuestionModule',
  components: {
    QuestionList
  },
  computed: {
    ...mapGetters({
      questions: '$_questions/questions',
      set: '$_questions/set'
    }),
    question_set () {
      // We will see what `params` is shortly
      return this.$route.params.questionSetId
    }
  },
  created () {
    const STORE_KEY = '$_questions'
    // eslint-disable-next-line no-underscore-dangle
    if (!(STORE_KEY in this.$store._modules.root._children)) {
      this.$store.registerModule(STORE_KEY, store)
    }
  },
  mounted () {
    this.$store.dispatch('$_questions/getQuestions', this.question_set)
    this.$store.dispatch('$_questions/getSet', this.question_set)
  }
}
</script>
