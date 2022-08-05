local Http = game:GetService('HttpService')

while true do
	local s,e = pcall(function()
		if game.ServerStorage.ALLSTOP.Value == false then
			local Data = Http:JSONDecode(Http:GetAsync('http://127.0.0.1/Data.json')) -- replace 127.0.0.1 with the ip/domain you are using
			local nub = 0
			for i, e in pairs(Data["data"]) do
				wait()
				for n, o in pairs(Data["data"][i]) do
					nub = nub+1
					script.Parent.Screen['P'..tostring(nub)].BackgroundColor3 = Color3.fromRGB(o[1], o[2], o[3])
				end
			end
		end
	end)
	if s then
		print('Updated')
	else
		print('ERROR')
	end
	wait(15)
end