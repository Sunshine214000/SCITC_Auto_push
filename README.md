# SCITC|智慧川信自动填报

<!-- wp:pullquote -->
<figure class="wp-block-pullquote"><blockquote><p>SCITC|智慧川信微信公众号健康信息自动填报</p><cite>微信公众号：木羽实验室</cite></blockquote></figure>
<!-- /wp:pullquote -->

<!-- wp:list -->
<ul><li>作者：Sunshine</li><li>微信公众号：木羽实验室</li><li>Sunshine Blog：https://muyu.fun/</li><li>声明：本项目仅供学习交流严禁使用于任何商业用途！</li>
</ul>

<!-- /wp:list -->

<!-- wp:heading -->
<h2>前言：</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p id="block-bb73bd83-d728-426c-8c76-95e0b4bf1bc2">🙂微信公众号每日自动提交健康信息python项目，目前支持QQ、邮件推送提交结果 <br>🙂本项目仅供学习交流使用，如作他用所承受的任何直接、间接法律责任一概与作者无关 <br>🙂如果此项目侵犯了您或者您公司的权益，请立即联系我删除</p>
<p>🔒本项目的源代码在MPL2.0协议下发布，同时附加以下条目：<p>
<p>非商业性使用 — 不得将此项目用于任何商业和盈利用途<p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>一、实现原理</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>通过抓包工具抓取微信公众号对应用用户的的OpenId，通过requests库，模拟手机等客户端携带cooick信息和表单信息向目标服务器提交post请求</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>二、使用方法</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>项目下载地址：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>蓝奏云：<a href="https://lee798.lanzoui.com/b0ag7xcod" target="_blank" rel="noreferrer noopener">https://lee798.lanzoui.com/b0ag7xcod</a>  密码:<span class="has-inline-color has-luminous-vivid-orange-color">cozl</span></li><li>阿里云盘：</li><li>GitHub：https://github.com/MY214000/SCITC_Auto_Health_information</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3>1.获取OpenId</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>获取方法已发布至微信公众号：<span class="has-inline-color has-luminous-vivid-amber-color">木羽实验室</span>，请关注后回复：<span class="has-inline-color has-pale-cyan-blue-color">获取openid</span>，获取相关文档教程</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>或者会抓包的小伙伴，建议使用Fidder进行抓包。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>2.填写配置信息</h3>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4>（1）用户配置信息</h4>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>users:
  - user:
    username: "木羽" # 备注信息
    Cookie_openid: "openid=*******" # 智慧川信公众获取的openid
    InSchool: "在校"
    GoOutYN: "在广元"
    lat: '32.4410401' # 纬度
    lon: '105.895168' # 经度
    qmsg_qq: "2140002006" # qmsg推送的qq号
    qmsg_key: "**************" # qmsg推送的key
    receiving_mailbox: "sunshine_poch@sina.com" # 收件邮箱
</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p><span class="has-inline-color has-pale-pink-color">注：关于qmsg使用方法请移步至：<a rel="noreferrer noopener" href="https://qmsg.zendee.cn/index.html" target="_blank">Qmsg公酱</a> 获取密钥和查看相关使用文档</span></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>配置信息支持多用户只需添加-user格式如下：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>users:
  - user:
    username: "" 
    Cookie_openid: "openid=*******"
    InSchool: ""
    GoOutYN: ""
    lat: ''
    lon: ''
    qmsg_qq: "" 
    qmsg_key: ""
    receiving_mailbox: ""
  - user:
    username: ""
    Cookie_openid: ""
    InSchool: ''
    GoOutYN: ""
    lat: ''
    lon: ''
    qmsg_qq: ""
    qmsg_key: ""
    receiving_mailbox: ""</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>（2）推送邮箱SMTP配置邮箱</h4>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>Smtp('qq邮箱smtp服务器', '发件人邮箱', 'SMTP密钥', '发件人邮箱',&#91;user&#91;'receiving_mailbox']]).sendmail(sendStr, '智慧川信公众号签到情况')</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p><span class="has-inline-color has-pale-pink-color">  注 ：关于查看相关使用文档 </span><br></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>3.运行测试及部署</h3>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>若输出状态码为：200 &amp;&amp; 若输出响应内容为：打卡成功    则测试成功，如遇其他问题请及时反馈</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>本项目支持：本地计划，Linux服务器定时任务，腾讯云云函数、阿里云函数等环境</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>如遇到任何问题请点击文章尾部联系作者进行询问或反馈</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>三、注意事项</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li><span class="has-inline-color has-vivid-red-color">使用、修改、转载、参考该项目，请标明原作者</span></li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p> 如果此项目<span class="has-inline-color has-vivid-red-color">侵犯了您或者您公司的权益，请立即联系我删除 ！！！</span></p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-fill"} -->
<div class="wp-block-button is-style-fill"><a class="wp-block-button__link" href="https://github.com/MY214000/SCITC_Auto_Health_information" target="_blank" rel="noreferrer noopener">github项目地址</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-fill"} -->
<div class="wp-block-button is-style-fill"><a class="wp-block-button__link" href="https://muyu.fun/wp-content/uploads/2021/09/微信图片_20210919135216.jpg" target="_blank" rel="noreferrer noopener">关注公众号</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-fill"} -->
<div class="wp-block-button is-style-fill"><a class="wp-block-button__link" href="http://wpa.qq.com/msgrd?v=3&amp;uin=2140002006&amp;site=qq&amp;menu=yes" target="_blank" rel="noreferrer noopener">联系作者</a></div>
<!-- /wp:button -->

<!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link" href="http://mail.qq.com/cgi-bin/qm_share?t=qm_mailme&amp;email=1qWjuKW_v7iz_Ka5tb6Wp6f4tbm7" target="_blank" rel="noreferrer noopener">邮件反馈</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->
