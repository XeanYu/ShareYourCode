
// 渲染WangEditor编辑器
var E = window.wangEditor;
var editor = new E('#editor');
editor.customConfig.uploadImgShowBase64 = true;
editor.create();

// 文章标题
var title;
swal({
      title: "标题",
      text: "代码标题",
      type: "input",
      showCancelButton: true,
      closeOnConfirm: false,
      animation: "slide-from-top",
      inputPlaceholder: "输入标题"
    },
    function(inputValue){
      if (inputValue === false) returnfalse;

      if (inputValue === "") {
        swal.showInputError("你需要输入一个标题");
        return false
      }

      swal("Good", "代码标题：" + inputValue,"success");
      title = inputValue;
      document.getElementById('title').innerText = title;
    });

// Ajax前端传后端
// 当提交按钮被点击时
document.getElementById('submit_code').addEventListener('click', function () {
        var code = {'code': editor.txt.html(), 'title': title}; // 组织数据
        $.ajax({
            type: 'POST', // 方法
            url: '/submit_code/', // 路径
            data: code, // 数据
            // 当进行传输时
            beforeSend: function () {
                swal({
                    title: "请稍后..",
                    text: "<div class=\"mdui-progress\">\n" +
                    "  <div class=\"mdui-progress-indeterminate\"></div>\n" +
                    "</div>",
                    html: true,
                });
            },
            // 传输成功时
            success: function (data) {
                if (data.msg) {
                    swal({
                        title: "成功",
                        text:"<strong>您的链接: http://"+ location.host + '/' + data.code_id + '/' +"</strong>",
                        html: true
                    });
                }
            },
            // 传输失败时
            error: function () {
                swal('失败', '请稍后重试..', 'error')
            }
        }); //aa
    }, false);