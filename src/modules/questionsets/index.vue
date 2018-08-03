<template>
  <QuestionSetList :question_sets="question_sets" />
</template>

<script>
import { mapGetters } from 'vuex'
import store from './_store'
import QuestionSetList from './_components/QuestionSetList'

export default {
  name: 'QuestionSetModule',
  components: {
    QuestionSetList
  },
  computed: {
    ...mapGetters({
      question_sets: '$_question_sets/questionSets'
    }),
    chapter () {
      return this.$route.params.chapterId
    }
  },
  created () {
    const STORE_KEY = '$_question_sets'
    // eslint-disable-next-line no-underscore-dangle
    if (!(STORE_KEY in this.$store._modules.root._children)) {
      this.$store.registerModule(STORE_KEY, store)
    }
  },
  mounted () {
    this.$store.dispatch('$_question_sets/getQuestionSets', this.chapter)
  }
}
</script>
