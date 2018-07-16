<template>
  <tr>
    <td v-text="course.name"></td>
  </tr>
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
