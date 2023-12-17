<template>
    
</template>
<script>
// 为给定 ID 的 user 创建请求
axios.get('http://127.0.0.1/history')
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
</script>