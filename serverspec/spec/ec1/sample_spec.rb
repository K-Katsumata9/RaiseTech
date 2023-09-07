require 'spec_helper'

listen_port = 80

describe package('nginx.x86_64') do
  it { should be_installed }
end

describe service('nginx') do
  it { should be_running }
end

describe package('git') do
  it { should be_installed }
end   

# 複数のパッケージがインストールされているかまとめて確認する
%w{mysql-community-client.x86_64 openssl.x86_64 ImageMagick.x86_64}.each do |pkg|
	describe package(pkg) do
    it { should be_installed }
  end
end

describe port(listen_port) do
  it { should be_listening }
end

describe port(8080) do
  it { should be_listening.with('tcp') }
end

describe command('ls -al') do
  its(:stdout) { should match /raisetech-live8-sample-app/ }
end