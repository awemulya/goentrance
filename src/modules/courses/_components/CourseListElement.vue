<template>
<v-flex text-xs-center>
          <v-card >
          <v-card-text class="px-0"><router-link :to="{ name: 'Subject', params: { courseId: course.id }}">{{course.name}}</router-link></v-card-text>
        </v-card>
</v-flex>
</template>

<script>
export default {
  name: 'CoursetListElement',
  props: {
    course: {
      type: Object
    }
  }
}
</script>
