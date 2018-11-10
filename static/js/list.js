$(function(){
//侧边栏点击回到顶部
	$("#sidebar_list li").click(function(e){
		e.stopPropagation();
		e.preventDefault();
		
	});
	
	$(".boder").click(function(){
//			console.log("aaa")
		$("html,body").stop(true).animate({scrollTop: 0}, 1000);
	})
	
	$("#sidebar_list li").eq(0).mouseenter(function(){
		$($(this)).html("客服咨询");
	})
	$("#sidebar_list li").eq(0).mouseleave(function(){
		$($(this)).html("<a href='#'><img src='../img/sidebarImg/2.png' /></a>");
	})
	
	
	
	$("#sidebar_list li").eq(1).mouseenter(function(){
		$($(this)).html("微信资讯");
		$("#weixin").css({"display":"block"});
	})
	
	$("#sidebar_list li").eq(1).mouseleave(function(){
		$($(this)).html("<a href='#'><img src='../img/sidebarImg/4.png' /></a>");
		$("#weixin").css({"display":"none"});
	})
	
	$("#sidebar_list li").eq(2).mouseenter(function(){
		$($(this)).html("app下载");
		$("#app").css({"display":"block"});
	})
	
	$("#sidebar_list li").eq(2).mouseleave(function(){
		$($(this)).html("<a href='#'><img src='../img/sidebarImg/1.png' /></a>");
		$("#app").css({"display":"none"});
	})
	
	$("#sidebar_list li").eq(3).mouseenter(function(){
		$($(this)).html("回到顶部");
	})
	
	$("#sidebar_list li").eq(3).mouseleave(function(){
		$($(this)).html("<a href='#'><img src='../img/sidebarImg/3.png' /></a>");
	})

    //    swiper
   new Swiper('.swiper-container', {
            pagination: '.swiper-pagination',
            paginationClickable: true,
            nextButton: '.swiper-button-next',
            prevButton: '.swiper-button-prev',
            speed: 2000,
            loop: true,
            observer:true,
            observeParents:true,
            autoplayDisableOnInteraction : false,
            autoplay:1500
    });

	//加载商品列表页的数据
	
	//ajax请求数据  动态加载到页面的指定位置
	$.get("/ajax/",function(data){
		console.log(arr);
		var arr = data.goodslist;
		//遍历数组中的数据
		for (var i=0;i<arr.length;i++) {
			var obj = arr[i];
			imgsrc = '/static/' + obj.img2
//			var li = "<li><div><img src='../"+obj.img2+"' /></div><p>"+obj.name+"</p><p>耐克</p><span><i>￥</i>"+obj.price+"</span></li>"
				var li= `<li>
							<div>
								<img src='${imgsrc}'>
							</div>
							<p>${obj.name}</p>
							<p>${obj.brand}</p>
							<span><i>￥</i>${obj.price}</span>
						</li>`

				//Es6模版字符串非常的好用
			$(li).appendTo($("#shoes_list"));

		}
//
		//点击尚品进入详情页
		$("#shoes_list").on("click","li",function(){
			var index = $(this).index();
			var obj = arr[index];
			//进入详情页， 且将当前点击的商品的id传入
			location.href = "/detail/?id=" + obj.id;
			console.log("aaaa")
		});
		//鼠标移入列表页时改变图片对应的src
		$("#shoes_list").on("mouseenter","img",function(){
			var index = $(this).index("#shoes_list img");
			var obj = arr[index];
			imgsrc1 = '/static/' + obj.img1
			// $(this).attr("src",imgsrc1);//这里src的路径是一样的
			$(this).attr('src',imgsrc1)

		});
		$("#shoes_list").on("mouseleave","img",function(){
			var index = $(this).index("#shoes_list img");
			var obj = arr[index];
			imgsrc = '/static/' + obj.img2
			$(this).attr('src',imgsrc);
		});

	});



})