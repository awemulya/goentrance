<template>
  <tr>
    <td><router-link :to="{ name: 'Chapter', params: { subjectId: subject.id }}">{{subject.name}}</router-link></td>
  </tr>
</template>

<script>
export default {
  name: 'SubjectListElement',
  props: {
    subject: {
      type: Object
    }
  }
}
</script>
