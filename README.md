<p># SCITC_Auto_push<br /># 现已重写完成，已提交代码至此仓库。感谢支持💖💖💖<br /># 技术交流SCITC|吹牛逼交流群：<a href="https://qm.qq.com/cgi-bin/qm/qr?k=qaRwaSma5K8xWpTFY95q9_6YI58QnABi&amp;jump_from=webapi" target="_blank" rel="noreferrer noopener">513816686</a><br />SCITC_Auto_Health_information的重写修复版本（）</p>

<!-- wp:pullquote -->
<figure class="wp-block-pullquote"><blockquote><p>SCITC|智慧川信微信公众号健康信息自动填报</p><cite>微信公众号：木羽实验室</cite></blockquote></figure>
<!-- /wp:pullquote -->

<!-- wp:list -->
<ul><li>作者：Sunshine</li><li>微信公众号：木羽实验室</li><li>Sunshine Blog：https://muyu.fun/</li><li>声明：本项目仅供学习交流严禁使用于任何商业用途！</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>前言：</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p id="block-bb73bd83-d728-426c-8c76-95e0b4bf1bc2">🙂微信公众号每日自动提交健康信息python项目，目前支持QQ、邮件推送提交结果 <br>🙂本项目仅供学习交流使用，如作他用所承受的任何直接、间接法律责任一概与作者无关 <br>🙂如果此项目侵犯了您或者您公司的权益，请立即联系我删除</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>一、实现原理</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>还是老样子通过抓包工具抓取某公众号对应用用户的cooick信息，通过requests库，模拟手机等客户端携带cooick信息定期get相关API，保持cooick信息存活，指定时间爬取表单信息，向目标服务器提交post请求</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>二、使用方法</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>项目下载地址：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>阿里云盘：<a href="https://www.aliyundrive.com/s/KstcVgUZfqN" target="_blank" rel="noreferrer noopener">https://www.aliyundrive.com/s/KstcVgUZfqN</a> 提取码：zy54</li><li>GitHub：<a href="https://github.com/Sunshine214000/SCITC_Auto_push">Sunshine214000/SCITC_Auto_push: SCITC_Auto_Health_information的重写修复版本 (github.com)</a></li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3>1.抓cooick信息</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>获取方法已发布至微信公众号：<span class="has-inline-color has-luminous-vivid-amber-color">木羽实验室</span>，请关注后回复：<span class="has-inline-color has-pale-cyan-blue-color">抓包教程</span>，获取相关文档教程</p>
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
<pre class="wp-block-code"><code>
###############################################################################
#     本项目的源代码在MPL2.0协议下发布，同时附加以下条目：                          #
#        非商业性使用 — 不得将此项目用于任何商业和盈利用途                          #
###############################################################################
users:
  - user:
    username: "木羽" # 备注信息
    code: "" # 智慧川信临时code
    Cookie: ""
    Temperature: "" # 体温
    InSchool: "在校　"
    GoOutYN: "在广元　"
    lat: '32.418995' # 维度
    lon: '105.88456' # 经度
    qq_gid: "" # 推送的qq群号
</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p><mark style="background-color:rgba(0, 0, 0, 0)" class="has-inline-color has-pale-pink-color">注：关于QQ推送框架搭建方法请移步至 <a href="https://docs.go-cqhttp.org/">go-cqhttp</a>  查看相关使用文档</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>!!!!不再支持多用户配置使用!!!!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>（2）推送go-cqhttp框架</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>在Auto_push_main.py中19与20行请更改为自己的服务器地址和端口号</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>    host = '' #推送go-cqhttp服务器主机地址
    client.connect((host, 5700))  # 端口</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p><mark style="background-color:rgba(0, 0, 0, 0)" class="has-inline-color has-pale-pink-color">  注 ：关于查看相关使用文档 </mark><br></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>3.运行测试及部署</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":51,"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full"><img src="https://muyu.fun/wp-content/uploads/2022/04/QQ图片20220406205857.jpg" alt="" class="wp-image-51"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>注意事项：</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>pip install -r requirements.txt 安装项目依赖库</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Linux关闭会话会使进程一并关闭，请使用nohup命令，相关用法请自行百度</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>如遇到任何问题请点击文章尾部联系作者进行询问或反馈</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>三、注意事项</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li><mark style="background-color:rgba(0, 0, 0, 0)" class="has-inline-color has-vivid-red-color">使用、修改、转载、参考该项目，请标明原作者</mark></li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p> 如果此项目<span class="has-inline-color has-vivid-red-color">侵犯了您或者您公司的权益，请立即联系我删除 ！！！</span></p>
<!-- /wp:paragraph -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button {"className":"is-style-fill"} -->
<div class="wp-block-button is-style-fill"><a class="wp-block-button__link" href="https://github.com/Sunshine214000/SCITC_Auto_push" target="_blank" rel="noreferrer noopener">github项目地址</a></div>
<!-- /wp:button -->

<!-- wp:button {"className":"is-style-fill"} -->
<div class="wp-block-button is-style-fill"><a class="wp-block-button__link" href="https://muyu.fun/sample-page/" target="_blank" rel="noreferrer noopener">关注公众号</a></div>
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
