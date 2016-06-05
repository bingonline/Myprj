/**
 * Created by home on 2016/6/4.
 */
$(function(){
    $('#box').datagrid({
        width : 400,
        url : '/data',
        title : '我爱你',
        iconCls : 'icon-search',
        columns :[[
            {
                field : "user",
                title : '账号',
            },
              {
                field : "email",
                title : '电子邮件',
            },
              {
                field : "date",
                title : '注册时间',
            },
        ]]
    });



});